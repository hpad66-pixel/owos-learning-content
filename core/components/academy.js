/* =====================================================================
   OWOS ACADEMY COMPONENT LIBRARY  (academy.js)
   Modules write declarative markup; this file renders and wires the real
   components. One place to fix, every module updates. Pairs with academy.css.

   A component is:
     <div data-ac="TYPE" data-title="..." data-kind="..." data-cue="Droobi note">
       <script type="application/json"> ...config... </script>
     </div>
   ===================================================================== */
(function(){
  "use strict";

  /* ---- Droobi mascot (injected once) ---- */
  function injectDroobi(){
    if(document.getElementById('ac-defs'))return;
    var s=document.createElementNS('http://www.w3.org/2000/svg','svg');
    s.id='ac-defs';s.setAttribute('aria-hidden','true');s.style.position='absolute';s.style.width='0';s.style.height='0';s.style.overflow='hidden';
    s.innerHTML='<symbol id="droobi" viewBox="0 0 64 64"><path d="M32 5C32 5 12 30 12 43a20 20 0 0 0 40 0C52 30 32 5 32 5Z" fill="#0A78BA"/><path d="M32 12C32 12 18 31 18 42a14 14 0 0 0 8 12.6C22 50 21 44 24 38c2.4-4.8 6-9 8-13 0 0 1-8 0-13Z" fill="#3E9BD6" opacity=".7"/><circle cx="26" cy="42" r="3.4" fill="#fff"/><circle cx="38" cy="42" r="3.4" fill="#fff"/><circle cx="26.8" cy="42.6" r="1.5" fill="#0F1728"/><circle cx="38.8" cy="42.6" r="1.5" fill="#0F1728"/><path d="M27 49q5 3 10 0" stroke="#0F1728" stroke-width="1.6" fill="none" stroke-linecap="round"/></symbol>';
    document.body.appendChild(s);
  }
  function droocue(msg){
    return '<div class="droocue"><svg class="av" viewBox="0 0 64 64"><use href="#droobi"/></svg><div class="m">'+msg+'</div></div>';
  }
  function shell(el, body){
    var t=el.dataset.title||'', k=el.dataset.kind||'', cue=el.dataset.cue||'';
    var h='<div class="comp">';
    if(t||k)h+='<div class="hd"><span>'+t+'</span>'+(k?'<span class="kind">'+k+'</span>':'')+'</div>';
    h+='<div class="bd">'+body+'</div>';
    if(cue)h+=droocue(cue);
    h+='</div>';
    el.innerHTML=h;
    return el.querySelector('.bd');
  }
  // Randomize answer order so learners cannot pattern-match on position.
  // Authors write the correct answer wherever it reads best; the learner never sees a fixed slot.
  function shuffled(list){
    var a=(list||[]).slice();
    for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),t=a[i];a[i]=a[j];a[j]=t;}
    return a;
  }

  function cfgOf(el){
    var s=el.querySelector('script[type="application/json"]');
    if(!s)return {};
    try{return JSON.parse(s.textContent);}catch(e){console.error('academy: bad config',el,e);return {};}
  }
  function shuffle(a){var r=a.slice();for(var i=r.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var t=r[i];r[i]=r[j];r[j]=t;}return r;}

  /* ---- tooltip: exactly one element for the whole page ---- */
  var TT;
  function initTooltips(){
    TT=document.getElementById('ac-tt');
    if(!TT){TT=document.createElement('div');TT.id='ac-tt';document.body.appendChild(TT);}
    function show(el){
      var def=el.getAttribute('data-def');if(!def)return;
      TT.innerHTML='<b>'+(el.getAttribute('data-term')||el.textContent)+'</b>'+def;
      TT.style.opacity='1';
      var r=el.getBoundingClientRect();
      var tw=Math.min(300,TT.offsetWidth||300);
      var x=r.left+r.width/2-tw/2;
      x=Math.max(10,Math.min(x,window.innerWidth-tw-10));
      var y=r.top-TT.offsetHeight-9;
      if(y<8)y=r.bottom+9;
      TT.style.left=x+'px';TT.style.top=y+'px';
    }
    function hide(){TT.style.opacity='0';}
    document.querySelectorAll('.term[data-def]').forEach(function(el){
      el.setAttribute('tabindex','0');
      el.removeAttribute('title'); // never a second, native tooltip
      el.addEventListener('mouseenter',function(){show(el);});
      el.addEventListener('mouseleave',hide);
      el.addEventListener('focus',function(){show(el);});
      el.addEventListener('blur',hide);
    });
    window.addEventListener('scroll',hide,true);
  }

  /* ---- lens toggle, reading progress, goals ---- */
  function initChrome(){
    var lens=document.querySelector('.lens');
    if(lens){var active=lens.querySelector('button.on')||lens.querySelector('button');if(active&&!document.body.hasAttribute('data-lens'))document.body.setAttribute('data-lens',active.getAttribute('data-lens'));
      lens.querySelectorAll('button').forEach(function(b){
      b.addEventListener('click',function(){
        lens.querySelectorAll('button').forEach(function(x){x.classList.remove('on');});
        b.classList.add('on');
        document.body.setAttribute('data-lens',b.getAttribute('data-lens'));
      });
    });}
    var bar=document.getElementById('rprog');
    if(bar){window.addEventListener('scroll',function(){
      var h=document.documentElement,max=h.scrollHeight-h.clientHeight;
      bar.style.width=(max>0?(h.scrollTop/max*100):0)+'%';
    });}
    document.querySelectorAll('.goals li').forEach(function(li){
      li.addEventListener('click',function(){li.classList.toggle('on');});
    });
  }

  /* ===================== component renderers ===================== */
  var R={};

  R.flip=function(el){var c=cfgOf(el);var b=shell(el,
    '<div class="flips">'+(c.cards||[]).map(function(p,i){
      return '<div class="flip" data-i="'+i+'"><div class="fin"><div class="ff">'+p[0]+'</div><div class="fbk">'+p[1]+'</div></div><span class="hint">flip</span></div>';
    }).join('')+'</div>');
    b.querySelectorAll('.flip').forEach(function(f){f.addEventListener('click',function(){f.classList.toggle('on');});});
  };

  R.match=function(el){var c=cfgOf(el);var pairs=c.pairs||[];
    var left=pairs.map(function(p,i){return {t:p[0],id:i};});
    var right=shuffle(pairs.map(function(p,i){return {t:p[1],id:i};}));
    var b=shell(el,'<div class="match"><div class="mcol l">'+
      left.map(function(o){return '<button class="mitem" data-id="'+o.id+'">'+o.t+'</button>';}).join('')+
      '</div><div class="mcol r">'+
      right.map(function(o){return '<button class="mitem" data-id="'+o.id+'">'+o.t+'</button>';}).join('')+
      '</div></div><div class="ac-fb ok" data-done>All matched. Nicely done.</div>');
    var sel=null,done=0,total=pairs.length;
    var L=b.querySelectorAll('.mcol.l .mitem'),Rr=b.querySelectorAll('.mcol.r .mitem');
    L.forEach(function(x){x.addEventListener('click',function(){
      if(x.classList.contains('done'))return;
      L.forEach(function(y){y.classList.remove('sel');});x.classList.add('sel');sel=x;
    });});
    Rr.forEach(function(x){x.addEventListener('click',function(){
      if(!sel||x.classList.contains('done'))return;
      if(x.dataset.id===sel.dataset.id){
        x.classList.add('done');sel.classList.add('done');sel.classList.remove('sel');sel=null;done++;
        if(done===total)b.querySelector('[data-done]').classList.add('on');
      }else{
        x.classList.add('bad');setTimeout(function(){x.classList.remove('bad');},520);
      }
    });});
  };

  R.mc=function(el){var c=cfgOf(el);var b=shell(el,
    '<p class="acq">'+(c.q||'')+'</p>'+
    shuffled(c.options).map(function(o,i){return '<button class="opt" data-i="'+i+'" data-c="'+(o[1]?1:0)+'">'+o[0]+'</button>';}).join('')+
    '<div class="ac-fb" data-fb></div>');
    var fb=b.querySelector('[data-fb]'),done=false;
    b.querySelectorAll('.opt').forEach(function(o){o.addEventListener('click',function(){
      if(done)return;done=true;var ok=o.dataset.c==='1';
      b.querySelectorAll('.opt').forEach(function(x){if(x.dataset.c==='1')x.classList.add('right');});
      if(!ok)o.classList.add('wrong');
      fb.className='ac-fb on '+(ok?'ok':'no');fb.innerHTML=ok?(c.right||'Correct.'):(c.wrong||'Not quite.');
    });});
  };

  R.multi=function(el){var c=cfgOf(el);var b=shell(el,
    '<p class="acq">'+(c.q||'')+'</p>'+
    shuffled(c.options).map(function(o,i){return '<button class="opt" data-i="'+i+'" data-c="'+(o[1]?1:0)+'">'+o[0]+'</button>';}).join('')+
    '<button class="btn" data-check style="margin-top:6px">Check</button><div class="ac-fb" data-fb></div>');
    var fb=b.querySelector('[data-fb]'),done=false;
    b.querySelectorAll('.opt').forEach(function(o){o.addEventListener('click',function(){if(!done)o.classList.toggle('sel');});});
    b.querySelector('[data-check]').addEventListener('click',function(){
      if(done)return;done=true;var good=true;
      b.querySelectorAll('.opt').forEach(function(x){
        var want=x.dataset.c==='1',got=x.classList.contains('sel');
        if(want)x.classList.add('right');
        if(got&&!want){x.classList.add('wrong');good=false;}
        if(!got&&want)good=false;
        x.classList.remove('sel');
      });
      fb.className='ac-fb on '+(good?'ok':'no');fb.innerHTML=good?(c.ok||'You got the full set.'):(c.no||'Close. The green ones are the full correct set.');
    });
  };

  R.classify=function(el){var c=cfgOf(el);var buckets=c.buckets||[];
    var b=shell(el,(c.items||[]).map(function(it,i){
      return '<div class="sortitem" data-i="'+i+'" data-a="'+it[1]+'"><div class="lab">'+it[0]+'</div>'+
        '<div class="sbtns">'+buckets.map(function(bk,j){return '<button class="sbtn" data-j="'+j+'">'+bk+'</button>';}).join(' ')+'</div>'+
        '<div class="why">'+(it[2]||'')+'</div></div>';
    }).join('')+'<div class="ac-score" data-score></div>');
    var total=(c.items||[]).length,solved=0;var sc=b.querySelector('[data-score]');
    b.querySelectorAll('.sortitem').forEach(function(row){
      var ans=+row.dataset.a;
      row.querySelectorAll('.sbtn').forEach(function(btn){btn.addEventListener('click',function(){
        if(row.classList.contains('done'))return;
        if(+btn.dataset.j===ans){btn.classList.add('right');row.classList.add('done');
          row.querySelectorAll('.sbtn').forEach(function(x){x.disabled=true;});solved++;
          sc.innerHTML='Sorted <b>'+solved+'</b> of '+total+'.';
        }else{btn.classList.add('wrong');btn.disabled=true;}
      });});
    });
  };

  R.estimate=function(el){var c=cfgOf(el);
    var b=shell(el,'<p class="acq">'+(c.q||'')+'</p>'+
      '<div class="erow"><input type="range" min="'+(c.min||0)+'" max="'+(c.max||100)+'" step="'+(c.step||1)+'" value="'+(c.start!=null?c.start:c.min||0)+'"><span class="v" data-v></span></div>'+
      '<button class="btn" data-check>Check my estimate</button><div class="ac-fb" data-fb></div>');
    var rng=b.querySelector('input'),v=b.querySelector('[data-v]'),fb=b.querySelector('[data-fb]');
    var unit=c.unit||'';
    function fmt(n){return unit==='$'?('$'+Number(n).toLocaleString()):(Number(n).toLocaleString()+(unit?(' '+unit):''));}
    function upd(){v.textContent=fmt(rng.value);}rng.addEventListener('input',upd);upd();
    b.querySelector('[data-check]').addEventListener('click',function(){
      var g=+rng.value,ok=Math.abs(g-c.answer)<=(c.tol||0);
      fb.className='ac-fb on '+(ok?'ok':'no');
      fb.innerHTML=(ok?'Good estimate. ':'The answer is <b>'+fmt(c.answer)+'</b>. ')+(c.solution||'');
    });
  };

  R.calc=function(el){var c=cfgOf(el);
    var ins=c.inputs||[
      {id:'cost',label:'What it costs to build',sub:'up-front dollars',min:500,max:3000,step:50,value:1300,fmt:'money'},
      {id:'ben',label:'What it saves each year',sub:'fewer breaks, less lost water',min:20,max:400,step:10,value:180,fmt:'moneyyr'},
      {id:'life',label:'How long it lasts',sub:'years',min:10,max:75,step:5,value:50,fmt:'years'},
      {id:'rate',label:'Discount rate',sub:'roughly, the cost of money',min:1,max:10,step:0.5,value:4,fmt:'pct'}
    ];
    var body=ins.map(function(i){return '<div class="calcrow"><span class="nm">'+i.label+(i.sub?'<small>'+i.sub+'</small>':'')+
      '</span><span class="ip"><input type="range" data-id="'+i.id+'" min="'+i.min+'" max="'+i.max+'" step="'+i.step+'" value="'+i.value+'"><span class="rv" data-rv="'+i.id+'"></span></span></div>';}).join('');
    body+='<div class="out"><div class="o"><div class="k">NPV (today’s dollars)</div><div class="val" data-npv>&nbsp;</div></div>'+
      '<div class="o"><div class="k">Payback</div><div class="val" data-pb>&nbsp;</div></div>'+
      '<div class="o"><div class="k">Benefit-cost ratio</div><div class="val" data-bcr>&nbsp;</div></div></div>'+
      '<div class="chartrow"><div class="chartbox"><div class="cap">Your money over time (the curve)</div>'+
      '<svg viewBox="0 0 300 150" data-curve style="width:100%;border:1px solid var(--line);border-radius:10px;background:var(--surface-2)"></svg></div>'+
      '<div class="chartbox"><div class="cap">Spend vs get back (the chart)</div><div class="bars2" data-bars></div></div></div>'+
      '<div class="verdict" data-verdict></div>';
    var b=shell(el,body);
    function val(id){var el2=b.querySelector('input[data-id="'+id+'"]');return el2?+el2.value:0;}
    function money(k){var v=k*1000;if(Math.abs(v)>=1e6)return '$'+(v/1e6).toFixed(2)+'M';return '$'+Math.round(v/1000)+'k';}
    var fmt={money:money,moneyyr:function(v){return money(v)+'/yr';},years:function(v){return v+' years';},pct:function(v){return (+v).toFixed(1)+'%';}};
    function recalc(){
      ins.forEach(function(i){b.querySelector('[data-rv="'+i.id+'"]').textContent=(fmt[i.fmt]||String)(val(i.id));});
      var cost=val('cost'),ben=val('ben'),life=val('life'),r=val('rate')/100;
      var pvBen=r>0?ben*(1-Math.pow(1+r,-life))/r:ben*life;
      var npv=pvBen-cost,bcr=pvBen/cost,pb=ben>0?cost/ben:Infinity;
      b.querySelector('[data-npv]').innerHTML=(npv>=0?'+':'−')+money(Math.abs(npv));
      b.querySelector('[data-pb]').textContent=isFinite(pb)?pb.toFixed(1)+' years':'never';
      b.querySelector('[data-bcr]').textContent=isFinite(bcr)?bcr.toFixed(2):'n/a';
      var v=b.querySelector('[data-verdict]');
      if(npv>0){v.className='verdict go';v.innerHTML='Worth doing. Every dollar in gives back about $'+bcr.toFixed(2)+' over its life, and the curve crosses into positive around year '+(isFinite(pb)?Math.round(pb):'')+'.';}
      else{v.className='verdict no';v.innerHTML='At these numbers it does not pay off. NPV is negative, so it costs more than it gives back. You would need a bigger yearly saving, a longer life, or the project waits.';}
      // curve: discounted cumulative cash flow
      var x0=8,x1=292,y0=12,y1=126,pts=[],minV=-cost,maxV=Math.max(0,npv);
      for(var t=0;t<=life;t++){var cum=(r>0?ben*(1-Math.pow(1+r,-t))/r:ben*t)-cost;pts.push([t,cum]);if(cum<minV)minV=cum;if(cum>maxV)maxV=cum;}
      var span=(maxV-minV)||1;
      function X(t){return x0+t/life*(x1-x0);}function Y(vv){return y1-(vv-minV)/span*(y1-y0);}
      var zeroY=Y(0),poly=pts.map(function(p){return X(p[0]).toFixed(1)+','+Y(p[1]).toFixed(1);}).join(' '),cross='';
      if(pvBen>cost){for(var t2=1;t2<=life;t2++){var c0=(r>0?ben*(1-Math.pow(1+r,-(t2-1)))/r:ben*(t2-1))-cost,c1=(r>0?ben*(1-Math.pow(1+r,-t2))/r:ben*t2)-cost;
        if(c0<0&&c1>=0){var tx=t2-1+(0-c0)/(c1-c0);cross='<circle cx="'+X(tx).toFixed(1)+'" cy="'+zeroY.toFixed(1)+'" r="4" fill="#0E8A64"/><text x="'+X(tx).toFixed(1)+'" y="'+(zeroY-7).toFixed(1)+'" text-anchor="middle" font-size="9" fill="#0E8A64">payback</text>';break;}}}
      b.querySelector('[data-curve]').innerHTML=
        '<line x1="'+x0+'" y1="'+zeroY.toFixed(1)+'" x2="'+x1+'" y2="'+zeroY.toFixed(1)+'" stroke="#CDD6E1" stroke-width="1" stroke-dasharray="3 3"/>'+
        '<text x="'+x0+'" y="'+(zeroY-4).toFixed(1)+'" font-size="8" fill="#8595AB">break even</text>'+
        '<polyline points="'+poly+'" fill="none" stroke="#0A78BA" stroke-width="2.2"/>'+cross+
        '<text x="'+x0+'" y="148" font-size="8" fill="#8595AB">year 0</text>'+
        '<text x="'+x1+'" y="148" text-anchor="end" font-size="8" fill="#8595AB">year '+life+'</text>';
      var mx=Math.max(cost,pvBen)||1;
      b.querySelector('[data-bars]').innerHTML=
        '<div class="col"><span class="bv">'+money(cost)+'</span><div class="bar" style="height:'+(cost/mx*100)+'%;background:var(--ink-3)"></div><span class="bl">You spend</span></div>'+
        '<div class="col"><span class="bv">'+money(pvBen)+'</span><div class="bar" style="height:'+(pvBen/mx*100)+'%;background:'+(pvBen>=cost?'var(--brand)':'var(--red)')+'"></div><span class="bl">You get back</span></div>';
    }
    b.querySelectorAll('input').forEach(function(x){x.addEventListener('input',recalc);});recalc();
  };

  R.truefalse=function(el){var c=cfgOf(el);
    var b=shell(el,'<div class="tf">'+(c.items||[]).map(function(it,i){
      return '<div class="tfrow" data-a="'+(it[1]?1:0)+'"><span class="s">'+it[0]+'</span>'+
        '<button class="tfbtn" data-v="1">True</button><button class="tfbtn" data-v="0">False</button>'+
        '<span class="tfx">'+(it[2]||'')+'</span></div>';
    }).join('')+'</div>');
    b.querySelectorAll('.tfrow').forEach(function(row){
      var ans=row.dataset.a;var x=row.querySelector('.tfx');
      row.querySelectorAll('.tfbtn').forEach(function(btn){btn.addEventListener('click',function(){
        row.querySelectorAll('.tfbtn').forEach(function(y){y.disabled=true;});
        if(btn.dataset.v===ans)btn.classList.add('right');
        else{btn.classList.add('wrong');row.querySelector('.tfbtn[data-v="'+ans+'"]').classList.add('right');}
        x.classList.add('on');
      });});
    });
  };

  R.order=function(el){var c=cfgOf(el);var items=c.items||[];
    var idx=items.map(function(_,i){return i;});var disp=shuffle(idx);
    if(disp.join()===idx.join()&&items.length>1)disp=idx.slice().reverse();
    var b=shell(el,'<p class="acq">'+(c.q||'')+'</p><div class="order" data-list>'+
      disp.map(function(k){return '<div class="oi" data-k="'+k+'"><span class="t">'+items[k]+'</span>'+
        '<button class="ob" data-d="-1">&#8593;</button><button class="ob" data-d="1">&#8595;</button></div>';}).join('')+
      '</div><button class="btn" data-check>Check the order</button><div class="ac-fb" data-fb></div>');
    var list=b.querySelector('[data-list]'),fb=b.querySelector('[data-fb]');
    list.addEventListener('click',function(e){var btn=e.target.closest('.ob');if(!btn)return;
      var oi=btn.closest('.oi'),d=+btn.dataset.d;
      if(d<0&&oi.previousElementSibling)list.insertBefore(oi,oi.previousElementSibling);
      if(d>0&&oi.nextElementSibling)list.insertBefore(oi.nextElementSibling,oi);
    });
    b.querySelector('[data-check]').addEventListener('click',function(){
      var ks=[].map.call(list.querySelectorAll('.oi'),function(o){return +o.dataset.k;});
      var ok=ks.join()===idx.join();
      list.querySelectorAll('.oi').forEach(function(o,i){o.classList.toggle('ok',+o.dataset.k===i);});
      fb.className='ac-fb on '+(ok?'ok':'no');fb.innerHTML=ok?(c.ok||'That is the right sequence.'):(c.no||'Not yet. Keep nudging until each row turns green.');
    });
  };

  R.reflect=function(el){var c=cfgOf(el);
    el.innerHTML='<div class="check"><div class="q">'+(c.q||'')+'</div>'+
      '<details><summary>Show a way to think about it</summary><div class="a">'+(c.a||'')+'</div></details></div>';
  };

  R.spectrum=function(el){var c=cfgOf(el);var zones=c.zones||[];
    var b=shell(el,'<div class="splabels"><span>'+(c.left||'')+'</span><span>'+(c.right||'')+'</span></div>'+
      '<div class="sptrack"></div><input type="range" min="0" max="100" value="'+(c.start!=null?c.start:50)+'">'+
      '<div class="spout" data-out></div>');
    var rng=b.querySelector('input'),out=b.querySelector('[data-out]');
    function upd(){var v=+rng.value,z=zones[zones.length-1];
      for(var i=0;i<zones.length;i++){if(v<=zones[i].max){z=zones[i];break;}}
      out.innerHTML='<b>'+z.title+'</b><br>'+z.body;}
    rng.addEventListener('input',upd);upd();
  };

  R.table=function(el){var c=cfgOf(el);var rows=c.rows||[];
    function cell(cv){if(Array.isArray(cv))return '<span class="lvl '+cv[0]+'">'+cv[1]+'</span>';return cv;}
    var b=shell(el,'<div class="cmpwrap"><table class="cmp"><thead><tr>'+
      (c.headers||[]).map(function(h){return '<th>'+h+'</th>';}).join('')+'</tr></thead><tbody>'+
      rows.map(function(r,i){return '<tr data-i="'+i+'"><td class="m">'+r.name+'</td>'+
        (r.cells||[]).map(function(cv){return '<td>'+cell(cv)+'</td>';}).join('')+'</tr>';}).join('')+
      '</tbody></table></div><div class="cmpdetail" data-detail></div>');
    var det=b.querySelector('[data-detail]');
    b.querySelectorAll('.cmp tbody tr').forEach(function(tr){tr.addEventListener('click',function(){
      var r=rows[+tr.dataset.i];if(!r.detail)return;
      b.querySelectorAll('.cmp tbody tr').forEach(function(x){x.classList.remove('on');});tr.classList.add('on');
      det.className='cmpdetail on';det.innerHTML='<b>'+r.name+'.</b> '+r.detail;
    });});
  };

  R.recommender=function(el){var c=cfgOf(el);
    var b=shell(el,'<p class="acq">'+(c.prompt||'')+'</p><div class="recopts">'+
      (c.options||[]).map(function(o,i){return '<button class="recbtn" data-i="'+i+'">'+o.label+'</button>';}).join('')+
      '</div><div class="recout" data-out></div>');
    var out=b.querySelector('[data-out]');
    b.querySelectorAll('.recbtn').forEach(function(btn){btn.addEventListener('click',function(){
      b.querySelectorAll('.recbtn').forEach(function(x){x.classList.remove('on');});btn.classList.add('on');
      var o=c.options[+btn.dataset.i];out.className='recout on';out.innerHTML='<b>'+o.name+'.</b> '+o.why;
    });});
  };

  R.decide=function(el){var c=cfgOf(el);
    var lead=(c.flow||[]).map(function(x,i){return (i?'<span class="farrow">&#8594;</span>':'')+'<div class="fbox'+(x.q?' q':'')+'">'+(x.q||x)+'</div>';}).join('');
    var b=shell(el,(lead?'<div class="flow" style="margin-bottom:16px">'+lead+'</div>':'')+
      '<p class="acq">'+(c.q||'')+'</p><div class="recopts">'+
      (c.options||[]).map(function(o,i){return '<button class="fbtn" data-i="'+i+'">'+o.label+'</button>';}).join('')+
      '</div><div class="fresult" data-out></div>');
    var out=b.querySelector('[data-out]');
    b.querySelectorAll('.fbtn').forEach(function(btn){btn.addEventListener('click',function(){
      b.querySelectorAll('.fbtn').forEach(function(x){x.classList.remove('on');});btn.classList.add('on');
      out.className='fresult on';out.innerHTML=c.options[+btn.dataset.i].result;
    });});
  };

  R.triangle=function(el){var c=cfgOf(el);var L=c.labels||['Scope','Time','Cost'];
    var subs=c.subs||['how much work','weeks you have','budget and crews'];
    var NAMES=['Very low','Low','Medium','High','Very high'];var keys=['scope','time','cost'];
    var b=shell(el,'<div class="trirow"><svg class="trisvg" viewBox="0 0 260 230" data-svg></svg>'+
      '<div class="tricontrols">'+[0,1,2].map(function(i){return '<div class="ctl"><span class="nm">'+L[i]+
        '<small>'+subs[i]+'</small></span><span class="step" data-k="'+i+'"><button data-d="-1">&#8722;</button>'+
        '<span class="v" data-v="'+i+'">Medium</span><button data-d="1">+</button></span></div>';}).join('')+
      '<div class="qbadge" data-badge></div></div></div>');
    var tc=[2,2,2],CX=130,CY=118;
    function vert(ang,v){var r=48+v*15;return [CX+r*Math.cos(ang),CY+r*Math.sin(ang)];}
    function render(){
      [0,1,2].forEach(function(i){b.querySelector('[data-v="'+i+'"]').textContent=NAMES[tc[i]];});
      var q=Math.max(0,Math.min(100,100-(tc[0]-(tc[1]+tc[2])/2)*28));
      var s=vert(-Math.PI/2,tc[0]),t=vert(Math.PI*0.833,tc[1]),cc=vert(Math.PI*0.167,tc[2]);
      var qc=q>=75?'#0E8A64':q>=45?'#A97B0F':'#D64545',qr=10+q/100*24;
      b.querySelector('[data-svg]').innerHTML=
        '<polygon points="'+s[0]+','+s[1]+' '+cc[0]+','+cc[1]+' '+t[0]+','+t[1]+'" fill="rgba(10,120,186,.08)" stroke="#0A78BA" stroke-width="2.5" stroke-linejoin="round"/>'+
        '<circle cx="'+CX+'" cy="'+CY+'" r="'+qr+'" fill="'+qc+'"/>'+
        '<text x="'+CX+'" y="'+(CY+4)+'" text-anchor="middle" font-size="10" font-weight="700" fill="#fff">'+Math.round(q)+'</text>'+
        '<text x="'+s[0]+'" y="'+(s[1]-9)+'" text-anchor="middle" font-size="10" font-weight="600" fill="#0F1728">'+L[0]+'</text>'+
        '<text x="'+(t[0]-4)+'" y="'+(t[1]+16)+'" text-anchor="middle" font-size="10" font-weight="600" fill="#0F1728">'+L[1]+'</text>'+
        '<text x="'+(cc[0]+4)+'" y="'+(cc[1]+16)+'" text-anchor="middle" font-size="10" font-weight="600" fill="#0F1728">'+L[2]+'</text>'+
        '<text x="'+CX+'" y="215" text-anchor="middle" font-size="9" fill="#8595AB">the dot is quality, 0 to 100</text>';
      var badge=b.querySelector('[data-badge]');
      badge.style.background=q>=75?'var(--green-50)':q>=45?'#FBF3E2':'var(--red-50)';badge.style.color=qc;
      badge.innerHTML='Quality holding at <b>'+Math.round(q)+'%</b> ('+(q>=75?'in good shape':q>=45?'getting strained':'corners being cut')+')';
    }
    b.querySelectorAll('.step').forEach(function(st){var k=+st.dataset.k;
      st.querySelectorAll('button').forEach(function(btn){btn.addEventListener('click',function(){
        tc[k]=Math.max(0,Math.min(4,tc[k]+ +btn.dataset.d));render();});});});
    render();
  };

  R.process=function(el){var c=cfgOf(el);var ph=c.phases||[];
    var b=shell(el,'<div class="life">'+ph.map(function(p,i){
      return '<div class="lphase'+(i===0?' on':'')+'" data-i="'+i+'"><b>'+p.title+'</b><span>'+(p.sub||'')+'</span>'+
        (c.gate&&i<ph.length-1?'<span class="gate">&#9670;</span>':'')+'</div>';
    }).join('')+'</div><div class="ldetail" data-detail>'+(ph[0]?ph[0].detail:'')+'</div>');
    var det=b.querySelector('[data-detail]');
    b.querySelectorAll('.lphase').forEach(function(x){x.addEventListener('click',function(){
      b.querySelectorAll('.lphase').forEach(function(y){y.classList.remove('on');});x.classList.add('on');
      det.innerHTML=ph[+x.dataset.i].detail;
    });});
  };

  R.method=function(el){var c=cfgOf(el);
    shell(el,'<div class="method">'+(c.steps||[]).map(function(s,i){
      return '<div class="stepn"><div class="n">'+(i+1)+'</div><div class="tx"><b>'+s[0]+'</b> '+(s[1]||'')+'</div></div>';
    }).join('')+'</div>');
  };

  R.artifacttracker=function(el){var c=cfgOf(el);var items=c.items||[];
    var states=c.states||['Not started','Draft','Evidence noted','Reviewed'];
    var storageKey='owos:artifacttracker:'+(c.key||location.pathname);
    var saved={};try{saved=JSON.parse(localStorage.getItem(storageKey)||'{}')||{};}catch(e){saved={};}
    var b=shell(el,'<div class="at-summary"><div><b data-count></b><span data-note></span></div><div class="at-meter" aria-hidden="true"><i data-meter></i></div></div><div class="at-list">'+
      items.map(function(it,i){return '<article class="at-item" data-id="'+(it.id||i)+'"><div><b>'+it.label+'</b><p>'+(it.detail||'')+'</p></div><button type="button" class="at-state" aria-live="polite"></button></article>';}).join('')+
      '</div><button type="button" class="btn at-reset" data-reset>Reset this tracker</button>');
    function value(row){var id=row.dataset.id,v=Number(saved[id]);return Number.isFinite(v)?Math.max(0,Math.min(states.length-1,v)):0;}
    function paint(row){var v=value(row),btn=row.querySelector('.at-state');row.dataset.state=String(v);btn.textContent=states[v];btn.setAttribute('aria-label',row.querySelector('b').textContent+': '+states[v]+'. Select to move to the next status.');}
    function report(){var reviewed=0,active=0;[].forEach.call(b.querySelectorAll('.at-item'),function(row){var v=value(row);if(v>0)active++;if(v===states.length-1)reviewed++;});
      b.querySelector('[data-count]').textContent=reviewed+' of '+items.length+' reviewed';
      b.querySelector('[data-note]').textContent=active+' started';b.querySelector('[data-meter]').style.width=(items.length?reviewed/items.length*100:0)+'%';
      try{localStorage.setItem(storageKey,JSON.stringify(saved));}catch(e){}
    }
    b.querySelectorAll('.at-item').forEach(function(row){paint(row);row.querySelector('.at-state').addEventListener('click',function(){var id=row.dataset.id;saved[id]=(value(row)+1)%states.length;paint(row);report();});});
    b.querySelector('[data-reset]').addEventListener('click',function(){saved={};b.querySelectorAll('.at-item').forEach(paint);report();});report();
  };

  R.layerstack=function(el){var c=cfgOf(el);var layers=c.layers||[];
    var b=shell(el,'<div class="lsstack">'+layers.map(function(layer,i){
      return '<button type="button" class="lslayer'+(i===0?' on':'')+'" data-i="'+i+'" aria-pressed="'+(i===0?'true':'false')+'"><span class="lsnum">'+(layer.number||i+1)+'</span><span><b>'+layer.label+'</b><small>'+(layer.sub||'')+'</small></span></button>';
    }).join('')+'</div><div class="lsdetail" data-detail aria-live="polite">'+(layers[0]?layers[0].detail:'')+'</div>');
    var detail=b.querySelector('[data-detail]');
    b.querySelectorAll('.lslayer').forEach(function(button){button.addEventListener('click',function(){
      b.querySelectorAll('.lslayer').forEach(function(item){item.classList.remove('on');item.setAttribute('aria-pressed','false');});button.classList.add('on');button.setAttribute('aria-pressed','true');
      detail.innerHTML=layers[+button.dataset.i].detail||'';
    });});
  };

  R.beforeafter=function(el){var c=cfgOf(el);var before=c.before||{},after=c.after||{};
    function panel(kind,data){return '<div class="bapanel '+kind+'"><span class="balabel">'+(data.label||kind)+'</span><h4>'+(data.title||'')+'</h4><ul>'+(data.items||[]).map(function(item){return '<li>'+item+'</li>';}).join('')+'</ul></div>';}
    var b=shell(el,'<div class="bastage">'+panel('before',before)+'<div class="baafter" data-after>'+panel('after',after)+'</div><i class="badivider" data-divider aria-hidden="true"><span>&#8596;</span></i></div><div class="barange"><label>'+(c.rangeLabel||'Move from fragmented to governed')+'</label><input type="range" min="0" max="100" value="50" aria-label="'+(c.rangeLabel||'Before and after comparison')+'"><output data-value>50% governed</output></div><div class="banote" data-note aria-live="polite"></div>');
    var range=b.querySelector('input'),overlay=b.querySelector('[data-after]'),divider=b.querySelector('[data-divider]'),out=b.querySelector('[data-value]'),note=b.querySelector('[data-note]');
    function update(){var v=+range.value;overlay.style.clipPath='inset(0 '+(100-v)+'% 0 0)';divider.style.left=v+'%';out.textContent=v+'% governed';
      var notes=c.notes||[];var selected=notes[notes.length-1]||'';for(var i=0;i<notes.length;i++){if(v<=notes[i].max){selected=notes[i].body;break;}}note.innerHTML=selected;}
    range.addEventListener('input',update);update();
  };

  R.handoff=function(el){var c=cfgOf(el);var steps=c.steps||[],mode='fragmented',index=0,timer=null;
    var b=shell(el,'<div class="hotoggle"><button type="button" class="on" data-mode="fragmented">Fragmented handoff</button><button type="button" data-mode="governed">Governed handoff</button></div><div class="hochain" data-chain></div><div class="hoctrl"><button type="button" data-action="reset">Reset</button><button type="button" data-action="back">Back</button><button type="button" class="primary" data-action="next">Next handoff</button><button type="button" data-action="play">Play</button><span data-count></span></div><div class="honarr" data-narr aria-live="polite"></div>');
    var chain=b.querySelector('[data-chain]'),narr=b.querySelector('[data-narr]'),count=b.querySelector('[data-count]');
    function stop(){if(timer){clearInterval(timer);timer=null;}b.querySelector('[data-action="play"]').textContent='Play';}
    function paint(){chain.innerHTML=steps.map(function(step,i){var state=i<index?' done':i===index?' active':'';var message=mode==='fragmented'?step.risk:step.control;return '<div class="honode'+state+'"><span>'+(i+1)+'</span><b>'+step.label+'</b><small>'+(step.sub||'')+'</small>'+(i<steps.length-1?'<i>&#8594;</i>':'')+'</div>';}).join('');
      var step=steps[index]||{};narr.className='honarr '+(mode==='fragmented'?'warn':'ok');narr.innerHTML='<b>'+(step.label||'')+'.</b> '+(mode==='fragmented'?(step.risk||''):(step.control||''));count.textContent=(steps.length?index+1:0)+' of '+steps.length;
      b.querySelector('[data-action="back"]').disabled=index===0;b.querySelector('[data-action="next"]').disabled=index>=steps.length-1;}
    b.querySelectorAll('[data-mode]').forEach(function(button){button.setAttribute('aria-pressed',button.classList.contains('on')?'true':'false');button.addEventListener('click',function(){stop();mode=button.dataset.mode;index=0;b.querySelectorAll('[data-mode]').forEach(function(item){item.classList.remove('on');item.setAttribute('aria-pressed','false');});button.classList.add('on');button.setAttribute('aria-pressed','true');paint();});});
    b.querySelector('[data-action="reset"]').addEventListener('click',function(){stop();index=0;paint();});
    b.querySelector('[data-action="back"]').addEventListener('click',function(){stop();index=Math.max(0,index-1);paint();});
    b.querySelector('[data-action="next"]').addEventListener('click',function(){stop();index=Math.min(steps.length-1,index+1);paint();});
    b.querySelector('[data-action="play"]').addEventListener('click',function(){if(timer){stop();return;}index=0;paint();this.textContent='Pause';timer=setInterval(function(){if(index>=steps.length-1){stop();return;}index++;paint();},1400);});paint();
  };

  R.fragtax=function(el){var c=cfgOf(el);var settings=c.inputs||{};
    function setting(id,label,unit,min,max,step,value){var x=settings[id]||{};return {id:id,label:x.label||label,unit:x.unit||unit,min:x.min==null?min:x.min,max:x.max==null?max:x.max,step:x.step==null?step:x.step,value:x.value==null?value:x.value};}
    var inputs=[setting('decisions','Decision cycles each month','cycles',1,60,1,12),setting('people','People rebuilding each answer','people',1,20,1,5),setting('minutes','Minutes per person per cycle','minutes',10,360,10,90),setting('rework','Added rework and exception time','%',0,100,5,25),setting('cost','Loaded labor cost','$ / hour',25,180,5,65)];
    var b=shell(el,'<div class="ftinputs">'+inputs.map(function(input){return '<label><span><b>'+input.label+'</b><small>'+input.unit+'</small></span><input type="range" data-id="'+input.id+'" min="'+input.min+'" max="'+input.max+'" step="'+input.step+'" value="'+input.value+'"><output data-out="'+input.id+'"></output></label>';}).join('')+'</div><div class="ftkpis"><div><b data-hours></b><span>annual search and join hours</span></div><div><b data-rework></b><span>annual rework hours</span></div><div class="key"><b data-cost></b><span>direct labor planning estimate</span></div><div><b data-weeks></b><span>40-hour work weeks</span></div></div><div class="ftchart"><div class="ftcol"><b data-base-label></b><i data-base-bar></i><span>search and reconcile</span></div><div class="ftcol"><b data-rework-label></b><i class="rework" data-rework-bar></i><span>added rework</span></div></div><div class="ftnote">'+(c.note||'This is a planning estimate of direct labor only. Validate local cycle counts, time, cost, service consequences, and risk before using it in a funding decision.')+'</div>');
    function value(id){return +b.querySelector('input[data-id="'+id+'"]').value;}function money(n){return '$'+Math.round(n).toLocaleString();}
    function paint(){inputs.forEach(function(input){var v=value(input.id),text=input.id==='cost'?money(v):v.toLocaleString();if(input.id==='rework')text+='%';b.querySelector('[data-out="'+input.id+'"]').textContent=text;});
      var base=value('decisions')*12*value('people')*value('minutes')/60,rework=base*value('rework')/100,total=base+rework,cost=total*value('cost'),max=Math.max(base,rework,1);
      b.querySelector('[data-hours]').textContent=Math.round(base).toLocaleString();b.querySelector('[data-rework]').textContent=Math.round(rework).toLocaleString();b.querySelector('[data-cost]').textContent=money(cost);b.querySelector('[data-weeks]').textContent=(total/40).toFixed(1);
      b.querySelector('[data-base-label]').textContent=Math.round(base).toLocaleString()+' h';b.querySelector('[data-rework-label]').textContent=Math.round(rework).toLocaleString()+' h';b.querySelector('[data-base-bar]').style.height=Math.max(5,base/max*120)+'px';b.querySelector('[data-rework-bar]').style.height=Math.max(5,rework/max*120)+'px';}
    b.querySelectorAll('input').forEach(function(input){input.addEventListener('input',paint);});paint();
  };

  R.artifactbuilder=function(el){var c=cfgOf(el),fields=c.fields||[],key='owos:artifactbuilder:'+(c.key||location.pathname),saved={};
    try{saved=JSON.parse(localStorage.getItem(key)||'{}')||{};}catch(e){saved={};}
    var b=shell(el,'<div class="abnotice">'+(c.notice||'Use only non-sensitive working text here. Save controlled utility evidence in an approved repository.')+'</div><div class="abfields">'+fields.map(function(field){return '<label><b>'+field.label+'</b><small>'+(field.help||'')+'</small><textarea data-id="'+field.id+'" rows="'+(field.rows||3)+'" placeholder="'+(field.placeholder||'')+'"></textarea></label>';}).join('')+'</div><div class="abpreview"><span>'+(c.previewLabel||'Executive case preview')+'</span><pre data-preview></pre></div><div class="abactions"><button type="button" class="btn" data-copy>Copy preview</button><button type="button" class="btn" data-clear>Clear saved draft</button><span data-status aria-live="polite"></span></div>');
    var preview=b.querySelector('[data-preview]'),status=b.querySelector('[data-status]');
    function compose(){var text=c.template||'';fields.forEach(function(field){var v=saved[field.id]||'['+field.label+']';text=text.split('{'+field.id+'}').join(v);});return text;}
    function save(){try{localStorage.setItem(key,JSON.stringify(saved));status.textContent='Draft saved on this device.';}catch(e){status.textContent='Draft could not be saved in this browser.';}preview.textContent=compose();}
    fields.forEach(function(field){var input=b.querySelector('[data-id="'+field.id+'"]').value=saved[field.id]||'';b.querySelector('[data-id="'+field.id+'"]').addEventListener('input',function(){saved[field.id]=this.value.trim();save();});});save();
    b.querySelector('[data-copy]').addEventListener('click',async function(){try{await navigator.clipboard.writeText(compose());status.textContent='Preview copied. Move it into your approved Launch Pack workspace.';}catch(e){status.textContent='Copy was blocked. Select the preview text and copy it manually.';}});
    b.querySelector('[data-clear]').addEventListener('click',function(){saved={};fields.forEach(function(field){b.querySelector('[data-id="'+field.id+'"]').value='';});try{localStorage.removeItem(key);}catch(e){}save();status.textContent='Saved draft cleared.';});
  };

  R.twofig=function(el){var c=cfgOf(el);function box(o){return '<div class="box"><div class="cap">'+o.cap+'</div>'+o.svg+'<div class="note">'+o.note+'</div></div>';}
    shell(el,'<div class="twofig">'+box(c.left)+box(c.right)+'</div>');
  };

  R.tree=function(el){var c=cfgOf(el);
    function render(nodes){
      return '<ul class="tkids">'+(nodes||[]).map(function(n){
        var kids=n.children&&n.children.length;
        return '<li class="tnode"><div class="trow" data-d="'+encodeURIComponent(n.detail||'')+'">'+
          (kids?'<button class="ttoggle" type="button">+</button>':'<span class="tdot"></span>')+
          '<span class="tlabel">'+n.label+'</span></div>'+
          (kids?'<div class="tkidwrap" hidden>'+render(n.children)+'</div>':'')+'</li>';
      }).join('')+'</ul>';
    }
    var top='<div class="tree"><ul class="tkids root">'+(c.nodes||[]).map(function(n){
      var kids=n.children&&n.children.length;
      return '<li class="tnode"><div class="trow" data-d="'+encodeURIComponent(n.detail||'')+'">'+
        (kids?'<button class="ttoggle open" type="button">−</button>':'<span class="tdot"></span>')+
        '<span class="tlabel">'+n.label+'</span></div>'+
        (kids?'<div class="tkidwrap">'+render(n.children)+'</div>':'')+'</li>';
    }).join('')+'</ul></div><div class="tdetail" data-td></div>';
    var b=shell(el,top);var td=b.querySelector('[data-td]');
    b.querySelectorAll('.ttoggle').forEach(function(t){t.addEventListener('click',function(e){e.stopPropagation();
      var wrap=t.closest('.tnode').querySelector('.tkidwrap');if(!wrap)return;
      wrap.hidden=!wrap.hidden;t.classList.toggle('open',!wrap.hidden);t.textContent=wrap.hidden?'+':'−';});});
    b.querySelectorAll('.trow').forEach(function(r){r.addEventListener('click',function(){
      var d=decodeURIComponent(r.getAttribute('data-d')||'');if(!d)return;
      b.querySelectorAll('.trow').forEach(function(x){x.classList.remove('on');});r.classList.add('on');
      td.className='tdetail on';td.innerHTML=d;});});
  };

  R.gantt=function(el){var c=cfgOf(el);var tasks=c.tasks||[];
    var by={};tasks.forEach(function(t){by[t.id]=t;});
    function deps(t){return (t.deps||[]).map(function(d){return typeof d==='object'?{id:d.to||d.id,lag:d.lag||0}:{id:d,lag:0};});}
    var ES={},EF={},LS={},LF={};
    tasks.forEach(function(t){ES[t.id]=0;EF[t.id]=t.dur;});
    for(var i=0;i<tasks.length+1;i++){tasks.forEach(function(t){var es=0;deps(t).forEach(function(d){es=Math.max(es,EF[d.id]+d.lag);});ES[t.id]=es;EF[t.id]=es+t.dur;});}
    var proj=0;tasks.forEach(function(t){proj=Math.max(proj,EF[t.id]);});
    var succ={};tasks.forEach(function(t){succ[t.id]=[];});
    tasks.forEach(function(t){deps(t).forEach(function(d){succ[d.id].push({id:t.id,lag:d.lag});});});
    tasks.forEach(function(t){LF[t.id]=proj;LS[t.id]=proj-t.dur;});
    for(var j=0;j<tasks.length+1;j++){tasks.forEach(function(t){var lf=succ[t.id].length?Infinity:proj;succ[t.id].forEach(function(s){lf=Math.min(lf,LS[s.id]-s.lag);});LF[t.id]=lf;LS[t.id]=lf-t.dur;});}
    var unit=c.unit||'weeks';
    function pct(v){return (v/proj*100);}
    var rows=tasks.map(function(t){
      var fl=Math.round((LS[t.id]-ES[t.id])*100)/100,crit=fl<=0.001;
      var bar='<div class="gbar'+(crit?' crit':'')+'" style="left:'+pct(ES[t.id]).toFixed(1)+'%;width:'+pct(t.dur).toFixed(1)+'%"></div>';
      var slack=fl>0?'<div class="gslack" style="left:'+pct(EF[t.id]).toFixed(1)+'%;width:'+pct(fl).toFixed(1)+'%"></div>':'';
      return '<div class="grow" data-id="'+t.id+'"><span class="gname">'+t.name+'</span><span class="gtrack">'+bar+slack+'</span></div>';
    }).join('');
    var b=shell(el,'<div class="gantt"><div class="ginner">'+rows+
      '<div class="gaxis"><span>0</span><span>'+Math.round(proj/2)+' '+unit+'</span><span>'+proj+' '+unit+'</span></div></div></div>'+
      '<div class="glegend"><span><span class="sw" style="background:var(--gold)"></span>on the critical path (zero float)</span>'+
      '<span><span class="sw" style="background:var(--brand)"></span>has float</span>'+
      '<span><span class="sw" style="background:var(--line-2)"></span>slack</span></div>'+
      '<div class="gsum">Project finishes in <b>'+proj+' '+unit+'</b>. The gold bars are the critical path: slip any one and the whole job slips.</div>'+
      '<div class="gdetail" data-gd></div>');
    var gd=b.querySelector('[data-gd]');
    b.querySelectorAll('.grow').forEach(function(r){r.addEventListener('click',function(){
      var t=by[r.dataset.id],fl=Math.round((LS[t.id]-ES[t.id])*100)/100,crit=fl<=0.001;
      b.querySelectorAll('.grow').forEach(function(x){x.classList.remove('on');});r.classList.add('on');
      gd.className='gdetail on';
      gd.innerHTML='<b>'+t.name+'.</b> Starts week '+ES[t.id]+', finishes week '+EF[t.id]+'. Float: <b>'+fl+' '+unit+'</b>. '+
        (crit?'<span class="crit">On the critical path.</span> It has no slack, so any delay here pushes the finish date.':'It has '+fl+' '+unit+' of slack, so a small delay here will not move the finish date.')+
        (t.note?' '+t.note:'');
    });});
  };

  R.cpmsim=function(el){var c=cfgOf(el);var tasks=c.tasks||[];var unit=c.unit||'weeks';
    var by={};tasks.forEach(function(t){by[t.id]=t;});
    function deps(t){return (t.deps||[]).map(function(d){return typeof d==='object'?{id:d.to||d.id,lag:d.lag||0}:{id:d,lag:0};});}
    var ES={},EF={},LS={},LF={},rank={};
    tasks.forEach(function(t){ES[t.id]=0;EF[t.id]=t.dur;});
    for(var i=0;i<tasks.length+1;i++){tasks.forEach(function(t){var es=0;deps(t).forEach(function(d){es=Math.max(es,EF[d.id]+d.lag);});ES[t.id]=es;EF[t.id]=es+t.dur;});}
    var proj=0;tasks.forEach(function(t){proj=Math.max(proj,EF[t.id]);});
    var succ={};tasks.forEach(function(t){succ[t.id]=[];});
    tasks.forEach(function(t){deps(t).forEach(function(d){succ[d.id].push({id:t.id,lag:d.lag});});});
    tasks.forEach(function(t){LF[t.id]=proj;LS[t.id]=proj-t.dur;});
    for(var j=0;j<tasks.length+1;j++){tasks.forEach(function(t){var lf=succ[t.id].length?Infinity:proj;succ[t.id].forEach(function(s){lf=Math.min(lf,LS[s.id]-s.lag);});LF[t.id]=lf;LS[t.id]=lf-t.dur;});}
    function fl(id){return Math.round((LS[id]-ES[id])*100)/100;}
    function crit(id){return fl(id)<=0.001;}
    // rank = longest predecessor chain (columns)
    for(var k=0;k<tasks.length+1;k++){tasks.forEach(function(t){var r=0;deps(t).forEach(function(d){r=Math.max(r,rank[d.id]+1);});rank[t.id]=r||0;});}
    var topo=tasks.slice().sort(function(a,b){return rank[a.id]-rank[b.id];});
    // layout: x by rank, y by row within rank
    var cols={};topo.forEach(function(t){(cols[rank[t.id]]=cols[rank[t.id]]||[]).push(t.id);});
    var BW=104,BH=68,GX=24,GY=18,pos={},maxRow=0;
    Object.keys(cols).forEach(function(cn){cols[cn].forEach(function(id,row){pos[id]={x:(+cn)*(BW+GX),y:row*(BH+GY)+11};if(row>maxRow)maxRow=row;});});
    var maxCol=Math.max.apply(null,tasks.map(function(t){return rank[t.id];}));
    var cw=(maxCol+1)*(BW+GX)-GX,ch=(maxRow+1)*(BH+GY)-GY+22;
    // build step list
    var steps=[];
    topo.forEach(function(t){steps.push({type:'F',id:t.id});});
    topo.slice().reverse().forEach(function(t){steps.push({type:'B',id:t.id});});
    steps.push({type:'FL'});steps.push({type:'C'});
    var fIndex={},bIndex={};steps.forEach(function(s,ix){if(s.type==='F')fIndex[s.id]=ix;if(s.type==='B')bIndex[s.id]=ix;});
    var flIndex=steps.findIndex(function(s){return s.type==='FL';}),cIndex=steps.length-1;
    var critNames=tasks.filter(function(t){return crit(t.id);}).sort(function(a,b){return ES[a.id]-ES[b.id];}).map(function(t){return t.name;});
    // arrows svg
    function arrows(cur){
      var out='';
      tasks.forEach(function(t){deps(t).forEach(function(d){
        var a=pos[d.id],b2=pos[t.id];if(!a||!b2)return;
        var x1=a.x+BW,y1=a.y+BH/2,x2=b2.x,y2=b2.y+BH/2;
        var gold=cur>=cIndex&&crit(t.id)&&crit(d.id);
        out+='<path d="M'+x1+' '+y1+' C'+(x1+26)+' '+y1+','+(x2-26)+' '+y2+','+(x2-2)+' '+y2+'" fill="none" stroke="'+(gold?'#A97B0F':'#CDD6E1')+'" stroke-width="'+(gold?2.5:1.5)+'" marker-end="url(#cpmar'+(gold?'g':'')+')"/>';
      });});
      return out;
    }
    function nodeHTML(t,cur){
      var showF=cur>=fIndex[t.id],showB=cur>=bIndex[t.id],showFL=cur>=flIndex,isCrit=cur>=cIndex&&crit(t.id);
      var active=steps[cur]&&steps[cur].id===t.id;
      return '<div class="cnode'+(isCrit?' crit':'')+(active?' active':'')+'" style="left:'+pos[t.id].x+'px;top:'+pos[t.id].y+'px;width:'+BW+'px">'+
        (showFL?'<span class="cn-float">float '+fl(t.id)+'</span>':'')+
        '<div class="cn-top"><span class="cn-v'+(showF?' on':'')+'">ES '+ES[t.id]+'</span><span class="cn-v'+(showF?' on':'')+'">EF '+EF[t.id]+'</span></div>'+
        '<div class="cn-mid"><div class="cn-name">'+t.name+'</div><div class="cn-dur">'+t.dur+' '+unit+'</div></div>'+
        '<div class="cn-bot"><span class="cn-v'+(showB?' on':'')+'">LS '+LS[t.id]+'</span><span class="cn-v'+(showB?' on':'')+'">LF '+LF[t.id]+'</span></div></div>';
    }
    function narr(cur){
      if(cur<0)return 'Press <b>Step</b> or <b>Play</b> to watch the critical path get derived. First the forward pass fills in the earliest dates, then the backward pass fills in the latest, then float reveals the critical chain.';
      var s=steps[cur];
      if(s.type==='F'){var t=by[s.id],ds=deps(t);
        return '<b>Forward pass.</b> '+t.name+': '+(ds.length?'it waits on '+ds.map(function(d){return by[d.id].name+' (finishes '+EF[d.id]+')';}).join(' and ')+', so earliest start = '+ES[t.id]:'no predecessors, so earliest start = 0')+'. Earliest finish = '+ES[t.id]+' + '+t.dur+' = '+EF[t.id]+'.';}
      if(s.type==='B'){var t2=by[s.id],ss=succ[t2.id];
        return '<b>Backward pass.</b> '+t2.name+': '+(ss.length?'latest finish = the earliest of what follows = '+LF[t2.id]:'last on its branch, so latest finish = project finish = '+proj)+'. Latest start = '+LF[t2.id]+' − '+t2.dur+' = '+LS[t2.id]+'.';}
      if(s.type==='FL')return '<b>Float = latest start − earliest start.</b> Zero float means no slack: the activity has nowhere to move. Every zero-float badge is on the critical path.';
      return 'The unbroken chain of zero-float activities is the <span class="g">critical path</span>: '+critNames.join(' → ')+'. It sets the finish at <span class="g">'+proj+' '+unit+'</span>. Slip any gold activity and the whole job slips.';
    }
    var b=shell(el,
      '<div class="cpmstage"><div class="cpmcanvas" style="width:'+cw+'px;height:'+ch+'px">'+
      '<svg class="cpmsvg" width="'+cw+'" height="'+ch+'"><defs>'+
      '<marker id="cpmar" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0 0L6 3L0 6z" fill="#CDD6E1"/></marker>'+
      '<marker id="cpmarg" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0 0L6 3L0 6z" fill="#A97B0F"/></marker></defs><g data-arrows></g></svg>'+
      '<div data-nodes></div></div></div>'+
      '<div class="cpmkey"><span><span>ES/EF</span> earliest start/finish (top)</span><span><span>LS/LF</span> latest start/finish (bottom)</span><span>gold = zero float = critical</span></div>'+
      '<div class="cpmctrl"><button data-reset>&#8635; Reset</button><button data-back>&#8592; Back</button>'+
      '<button class="primary" data-step>Step &#8594;</button><button data-play>&#9654; Play</button>'+
      '<button data-end>Skip to critical path</button><span class="cpmstep" data-lbl></span></div>'+
      '<div class="cpmnarr" data-narr></div>');
    var cur=-1,timer=null;var canvas=b.querySelector('.cpmcanvas');
    var nodesEl=b.querySelector('[data-nodes]'),arrowsEl=b.querySelector('[data-arrows]'),narrEl=b.querySelector('[data-narr]'),lbl=b.querySelector('[data-lbl]');
    var phaseName=function(cur){if(cur<0)return 'ready';var t=steps[cur].type;return t==='F'?'forward pass':t==='B'?'backward pass':t==='FL'?'float':'critical path';};
    function draw(){
      arrowsEl.innerHTML=arrows(cur);
      nodesEl.innerHTML=tasks.map(function(t){return nodeHTML(t,cur);}).join('');
      narrEl.innerHTML=narr(cur);
      lbl.textContent='Step '+(cur+1)+' / '+steps.length+' · '+phaseName(cur);
      b.querySelector('[data-back]').disabled=cur<0;b.querySelector('[data-step]').disabled=cur>=steps.length-1;
    }
    function stop(){if(timer){clearInterval(timer);timer=null;b.querySelector('[data-play]').innerHTML='&#9654; Play';}}
    function step(){if(cur<steps.length-1){cur++;draw();}else stop();}
    b.querySelector('[data-step]').addEventListener('click',function(){stop();step();});
    b.querySelector('[data-back]').addEventListener('click',function(){stop();if(cur>=0){cur--;draw();}});
    b.querySelector('[data-reset]').addEventListener('click',function(){stop();cur=-1;draw();});
    b.querySelector('[data-end]').addEventListener('click',function(){stop();cur=steps.length-1;draw();});
    b.querySelector('[data-play]').addEventListener('click',function(){
      if(timer){stop();return;}
      if(cur>=steps.length-1)cur=-1;
      b.querySelector('[data-play]').innerHTML='&#10073;&#10073; Pause';
      timer=setInterval(function(){if(cur>=steps.length-1){stop();}else step();},1100);
    });
    // scale the fixed-width network down to fit the page width, so nothing runs off the right edge
    var stage=b.querySelector('.cpmstage');
    function fit(){var avail=stage.clientWidth||canvas.parentNode.clientWidth||700;var sc=Math.min(1,avail/(cw+42));
      if(sc>=0.999){canvas.style.transform='';stage.style.height='';}
      else{canvas.style.transformOrigin='top left';canvas.style.transform='scale('+sc.toFixed(3)+')';stage.style.height=Math.ceil(ch*sc+6)+'px';}
      stage.style.overflowX='hidden';}
    var ft;window.addEventListener('resize',function(){clearTimeout(ft);ft=setTimeout(fit,150);});
    window.addEventListener('load',fit);setTimeout(fit,400);
    draw();fit();
  };

  R.scurve=function(el){var c=cfgOf(el);var p=c.periods||[];
    var W=320,H=170,x0=30,x1=308,y0=14,y1=140;
    var cum=[],run=0;p.forEach(function(d){run+=d.spend;cum.push(run);});
    var total=run||1,maxSp=Math.max.apply(null,p.map(function(d){return d.spend;}))||1;
    function X(i){return x0+(p.length<=1?0:i/(p.length-1)*(x1-x0));}
    function Yc(v){return y1-v/total*(y1-y0);}
    var bars=p.map(function(d,i){var bw=(x1-x0)/p.length*0.6,bx=x0+(i+0.5)/p.length*(x1-x0)-bw/2,bh=d.spend/maxSp*(y1-y0)*0.55;
      return '<rect x="'+bx.toFixed(1)+'" y="'+(y1-bh).toFixed(1)+'" width="'+bw.toFixed(1)+'" height="'+bh.toFixed(1)+'" fill="#D3EAF8" rx="2"/>';}).join('');
    var line=cum.map(function(v,i){return X(i).toFixed(1)+','+Yc(v).toFixed(1);}).join(' ');
    var dots=cum.map(function(v,i){return '<circle cx="'+X(i).toFixed(1)+'" cy="'+Yc(v).toFixed(1)+'" r="2.6" fill="#0A78BA"/>';}).join('');
    var labels=p.map(function(d,i){return '<text x="'+X(i).toFixed(1)+'" y="'+(H-4)+'" text-anchor="middle" font-size="8" fill="#8595AB">'+d.label+'</text>';}).join('');
    var b=shell(el,'<div class="scurve"><svg viewBox="0 0 '+W+' '+H+'">'+
      '<line x1="'+x0+'" y1="'+y1+'" x2="'+x1+'" y2="'+y1+'" stroke="#CDD6E1"/>'+
      '<line x1="'+x0+'" y1="'+y0+'" x2="'+x0+'" y2="'+y1+'" stroke="#CDD6E1"/>'+
      bars+'<polyline points="'+line+'" fill="none" stroke="#0A78BA" stroke-width="2.4"/>'+dots+labels+
      '<text x="'+x0+'" y="'+(y0-3)+'" font-size="8" fill="#8595AB">'+(c.totalLabel||('total '+total))+'</text></svg></div>'+
      '<div class="sclegend"><span><span class="sw" style="background:#D3EAF8"></span>spend each period</span>'+
      '<span><span class="sw" style="background:var(--brand)"></span>cumulative (the S-curve)</span></div>');
  };

  R.costcurve=function(el){var c=cfgOf(el);var st=c.stages||[];
    var maxM=Math.max.apply(null,st.map(function(s){return s.mult;}))||1;
    function h(m){return Math.max(3,(Math.log(m)/Math.log(maxM))*100)+'%';}
    var b=shell(el,'<div class="ccbars">'+st.map(function(s,i){return '<div class="ccbar'+(i===0?' on':'')+'" data-i="'+i+'"><span class="m">'+s.mult+'x</span><div class="fill" style="height:'+h(s.mult)+'"></div></div>';}).join('')+
      '</div><div class="cclabels">'+st.map(function(s){return '<span>'+s.label+'</span>';}).join('')+'</div><div class="ccout" data-out></div>');
    var out=b.querySelector('[data-out]');
    function sel(i){b.querySelectorAll('.ccbar').forEach(function(x,j){x.classList.toggle('on',j===i);});var s=st[i];out.innerHTML='A problem caught at <b>'+s.label+'</b> costs about <b>'+s.mult+'x</b> to fix. '+(s.note||'');}
    b.querySelectorAll('.ccbar').forEach(function(x){x.addEventListener('click',function(){sel(+x.dataset.i);});});sel(0);
  };

  R.ripple=function(el){var c=cfgOf(el);var d=c.driver||{},eff=c.effects||[];
    var b=shell(el,'<div class="rpdriver"><span class="nm">'+(d.label||'Driver')+'</span><input type="range" min="'+(d.min||0)+'" max="'+(d.max||10)+'" step="'+(d.step||1)+'" value="'+(d.start||0)+'"><span class="v" data-dv></span></div>'+
      '<div class="rpeff">'+eff.map(function(e,i){return '<div class="rprow"><span class="lb">'+e.label+'</span><span class="rpmeter"><span class="rpfill" data-fill="'+i+'"></span></span><span class="val" data-val="'+i+'"></span></div>';}).join('')+'</div><div class="rpnote" data-note></div>');
    var rng=b.querySelector('input'),dv=b.querySelector('[data-dv]'),note=b.querySelector('[data-note]');
    function fmt(v,unit){if(unit==='$k'){var n=v*1000;return n>=1e6?'$'+(n/1e6).toFixed(2)+'M':'$'+Math.round(v)+'k';}return (Math.round(v*10)/10)+(unit?(' '+unit):'');}
    function upd(){var x=+rng.value;dv.textContent=x+(d.unit?(' '+d.unit):'');
      eff.forEach(function(e,i){var val=(e.base||0)+x*(e.per||0),mx=e.max||val||1,f=b.querySelector('[data-fill="'+i+'"]');
        f.style.width=Math.min(100,val/mx*100)+'%';f.style.background=(val/mx>0.85?'var(--red)':'var(--brand)');
        b.querySelector('[data-val="'+i+'"]').textContent=fmt(val,e.unit);});
      note.innerHTML=(x===(d.start||0))?(c.baseNote||'Move the slider. Watch every output move at once.'):'Adding <b>'+x+' '+(d.unit||'')+'</b> ripples into all three. Integration means you update them <b>together</b> and run the change through change control, not one in isolation.';}
    rng.addEventListener('input',upd);upd();
  };

  R.ganttedit=function(el){var c=cfgOf(el);var unit=c.unit||'weeks';
    var tasks=(c.tasks||[]).map(function(t){return {id:t.id,name:t.name,dur:t.dur,deps:t.deps||[]};});
    function deps(t){return (t.deps||[]).map(function(d){return typeof d==='object'?{id:d.to||d.id,lag:d.lag||0}:{id:d,lag:0};});}
    function compute(){var ES={},EF={},LS={},LF={};tasks.forEach(function(t){ES[t.id]=0;EF[t.id]=t.dur;});
      for(var i=0;i<tasks.length+1;i++)tasks.forEach(function(t){var es=0;deps(t).forEach(function(d){es=Math.max(es,EF[d.id]+d.lag);});ES[t.id]=es;EF[t.id]=es+t.dur;});
      var proj=0;tasks.forEach(function(t){proj=Math.max(proj,EF[t.id]);});
      var succ={};tasks.forEach(function(t){succ[t.id]=[];});tasks.forEach(function(t){deps(t).forEach(function(d){succ[d.id].push({id:t.id,lag:d.lag});});});
      tasks.forEach(function(t){LF[t.id]=proj;LS[t.id]=proj-t.dur;});
      for(var j=0;j<tasks.length+1;j++)tasks.forEach(function(t){var lf=succ[t.id].length?Infinity:proj;succ[t.id].forEach(function(s){lf=Math.min(lf,LS[s.id]-s.lag);});LF[t.id]=lf;LS[t.id]=lf-t.dur;});
      return {ES:ES,LS:LS,proj:proj};}
    var b=shell(el,'<div class="gantt"><div class="ginner" data-inner></div><div class="gaxis" data-axis style="margin-left:200px"></div></div>'+
      '<div class="glegend"><span><span class="sw" style="background:var(--gold)"></span>critical path</span><span><span class="sw" style="background:var(--brand)"></span>has float</span></div>'+
      '<div class="gsum" data-sum></div><div class="gd-note" data-note></div>');
    var inner=b.querySelector('[data-inner]'),axis=b.querySelector('[data-axis]'),sum=b.querySelector('[data-sum]'),note=b.querySelector('[data-note]'),lastCrit='';
    function fl(r,id){return Math.round((r.LS[id]-r.ES[id])*100)/100;}
    function render(){var r=compute();function pct(v){return v/r.proj*100;}
      inner.innerHTML=tasks.map(function(t){var crit=fl(r,t.id)<=0.001;
        return '<div class="grow"><span class="gname ed">'+t.name+'</span><span class="gstep" data-id="'+t.id+'"><button data-d="-1">-</button><button data-d="1">+</button></span><span class="gtrack"><span class="gbar'+(crit?' crit':'')+'" style="left:'+pct(r.ES[t.id]).toFixed(1)+'%;width:'+pct(t.dur).toFixed(1)+'%"></span></span></div>';}).join('');
      axis.innerHTML='<span>0</span><span>'+r.proj+' '+unit+'</span>';
      sum.innerHTML='Finish: <b>'+r.proj+' '+unit+'</b>. Change any duration and watch the critical path and the finish move.';
      var critNow=tasks.filter(function(t){return fl(r,t.id)<=0.001;}).map(function(t){return t.id;}).join(',');
      if(lastCrit&&critNow!==lastCrit){note.className='gd-note warn';note.innerHTML='The critical path just <b>changed</b>. Speeding up one chain can hand the lead to another, so the bottleneck moves somewhere new.';}
      else{note.className='gd-note';note.innerHTML='Shorten a <b>gold</b> (critical) task to pull the finish in. Shortening a blue task does nothing to the finish, it only buys that task more float.';}
      lastCrit=critNow;
      inner.querySelectorAll('.gstep').forEach(function(sp){var id=sp.dataset.id;sp.querySelectorAll('button').forEach(function(btn){btn.addEventListener('click',function(){var t=tasks.filter(function(x){return x.id===id;})[0];t.dur=Math.max(1,t.dur+ +btn.dataset.d);render();});});});}
    render();
  };

  R.rollup=function(el){var c=cfgOf(el);var unit=c.unit||'hrs',idc=0,map={};
    function prep(n){n._id='ru'+(idc++);map[n._id]=n;if(n.children)n.children.forEach(prep);}(c.nodes||[]).forEach(prep);
    function sum(n){return (n.children&&n.children.length)?n.children.reduce(function(a,ch){return a+sum(ch);},0):(+n.value||0);}
    function node(n){var kids=n.children&&n.children.length;
      return '<li><div class="rurow"><span class="runame'+(kids?' parent':'')+'">'+n.label+'</span>'+
        (kids?'<span class="rusum" data-sum="'+n._id+'"></span>':'<input class="ruinput" type="number" min="0" data-in="'+n._id+'" value="'+(+n.value||0)+'">')+'</div>'+
        (kids?'<ul class="rukids">'+n.children.map(node).join('')+'</ul>':'')+'</li>';}
    var b=shell(el,'<div class="rutotal"><span class="k">Project total</span><span class="v" data-total></span></div><ul class="rukids root">'+(c.nodes||[]).map(node).join('')+'</ul>');
    function refresh(){b.querySelectorAll('[data-sum]').forEach(function(sp){sp.textContent=sum(map[sp.dataset.sum])+' '+unit;});
      b.querySelector('[data-total]').textContent=(c.nodes||[]).reduce(function(a,n){return a+sum(n);},0)+' '+unit;}
    b.querySelectorAll('.ruinput').forEach(function(inp){inp.addEventListener('input',function(){map[inp.dataset.in].value=+inp.value||0;refresh();});});refresh();
  };

  R.scoreboard=function(el){var c=cfgOf(el);var crit=c.criteria||[],proj=c.projects||[];
    var b=shell(el,'<div class="sbcrit">'+crit.map(function(cr,i){return '<div class="sbcrow"><span class="lb">'+cr.label+'</span><input type="range" min="0" max="5" step="1" value="'+(cr.weight!=null?cr.weight:3)+'" data-w="'+i+'"><span class="w" data-wv="'+i+'"></span></div>';}).join('')+
      '</div><table class="sbtable"><thead><tr><th></th><th>Project</th><th>Score</th></tr></thead><tbody data-body></tbody></table>');
    var body=b.querySelector('[data-body]');
    function upd(){var w=crit.map(function(cr,i){return +b.querySelector('[data-w="'+i+'"]').value;}),wsum=w.reduce(function(a,x){return a+x;},0)||1;
      crit.forEach(function(cr,i){b.querySelector('[data-wv="'+i+'"]').textContent=w[i];});
      var scored=proj.map(function(p){var tot=crit.reduce(function(a,cr,i){return a+((p.scores&&p.scores[cr.key])||0)*w[i];},0)/wsum;return {name:p.name,score:tot};});
      scored.sort(function(a,b2){return b2.score-a.score;});var mx=Math.max.apply(null,scored.map(function(s){return s.score;}))||1;
      body.innerHTML=scored.map(function(s,i){return '<tr class="'+(i===0?'top':'')+'"><td class="rk">'+(i+1)+'</td><td><span class="pn">'+s.name+'</span><span class="sbbar"><i style="width:'+(s.score/mx*100).toFixed(0)+'%"></i></span></td><td class="sc">'+s.score.toFixed(1)+'</td></tr>';}).join('');}
    b.querySelectorAll('[data-w]').forEach(function(x){x.addEventListener('input',upd);});upd();
  };

  R.pv=function(el){var c=cfgOf(el);var amt=c.amount||1000;
    function m0(v){return '$'+Math.round(v).toLocaleString();}
    var b=shell(el,'<div class="pvrow"><span class="nm">Years from now</span><input type="range" min="0" max="'+(c.maxYears||50)+'" step="1" value="'+(c.startYears||20)+'" data-y><span class="v" data-yv></span></div>'+
      '<div class="pvrow"><span class="nm">Discount rate</span><input type="range" min="1" max="10" step="0.5" value="'+(c.startRate||4)+'" data-r><span class="v" data-rv></span></div>'+
      '<div class="pvbars"><div class="pvcol"><span class="bv">'+m0(amt)+'</span><div class="bar" style="height:100%;background:var(--ink-3)"></div><span class="bl">Value in the future</span></div>'+
      '<div class="pvcol"><span class="bv" data-pvv></span><div class="bar" data-pvbar style="background:var(--brand)"></div><span class="bl">Worth today</span></div></div><div class="pvout" data-out></div>');
    var yr=b.querySelector('[data-y]'),rr=b.querySelector('[data-r]');
    function upd(){var y=+yr.value,r=+rr.value/100;b.querySelector('[data-yv]').textContent=y+' yr';b.querySelector('[data-rv]').textContent=(r*100).toFixed(1)+'%';
      var pv=amt/Math.pow(1+r,y);b.querySelector('[data-pvv]').textContent=m0(pv);b.querySelector('[data-pvbar]').style.height=Math.max(2,pv/amt*100)+'%';
      b.querySelector('[data-out]').innerHTML=m0(amt)+' promised '+y+' years out is worth about <b>'+m0(pv)+'</b> today at '+(r*100).toFixed(1)+'%. That is why future savings are discounted: a dollar later is worth less than a dollar now. The formula is PV = FV / (1 + r) raised to the number of years.';}
    yr.addEventListener('input',upd);rr.addEventListener('input',upd);upd();
  };

  R.program=function(el){var c=cfgOf(el);var ps=c.projects||[],mx=c.maxMonths||36;
    var b=shell(el,ps.map(function(p,i){return '<div class="pvrow"><span class="nm">'+p.name+'</span><input type="range" data-i="'+i+'" min="'+(p.min||6)+'" max="'+mx+'" step="1" value="'+p.months+'"><span class="v" data-v="'+i+'"></span></div>';}).join('')+
      '<div class="pgbars" data-bars></div><div class="pgout" data-out></div><div class="pgnote" data-note></div>');
    function upd(){var vals=ps.map(function(p,i){return +b.querySelector('input[data-i="'+i+'"]').value;});
      var last=Math.max.apply(null,vals),driver=ps[vals.indexOf(last)];
      ps.forEach(function(p,i){b.querySelector('[data-v="'+i+'"]').textContent=vals[i]+' mo';});
      b.querySelector('[data-bars]').innerHTML=ps.map(function(p,i){var drives=vals[i]===last;
        return '<div class="pgrow"><span class="pn">'+p.name+'</span><span class="pt"><i class="'+(drives?'drv':'')+'" style="width:'+(vals[i]/mx*100)+'%"></i></span><span class="pm">'+vals[i]+'</span></div>';}).join('')+
        '<div class="pgrow ben"><span class="pn">'+(c.benefitName||'Benefit realized')+'</span><span class="pt"><i class="ben" style="width:'+(last/mx*100)+'%"></i></span><span class="pm">'+last+'</span></div>';
      b.querySelector('[data-out]').innerHTML='<b>'+(c.benefit||'The benefit')+'</b> arrives in month <b>'+last+'</b>, set by <b>'+driver.name+'</b>.';
      var early=vals.filter(function(v){return v<last;}).length;
      b.querySelector('[data-note]').innerHTML=early>0
        ? 'Notice what finishing early buys you: nothing. '+early+' of these '+(early===1?'project is':'projects are')+' done before month '+last+', and the benefit still waits for <b>'+driver.name+'</b>. Money spent accelerating anything except the driver is money spent for no earlier benefit. <b>A program manages the benefit, not the projects,</b> which is why a program manager pushes on the slowest component and leaves the others alone.'
        : 'Everything lands in the same month, so every project is a driver and there is no slack anywhere in the program. That is efficient and extremely fragile: any one slip moves the benefit.';}
    b.querySelectorAll('input').forEach(function(x){x.addEventListener('input',upd);});upd();
  };

  R.examsim=function(el){var c=cfgOf(el);var qs=c.questions||[],i=0,score=0,answered=false;
    var b=shell(el,'<div class="exhead"><span class="exq" data-pos></span><span class="exsc" data-score></span></div>'+
      '<p class="acq" data-q></p><div class="exopts" data-opts></div><div class="ac-fb" data-fb></div>'+
      '<button class="btn" data-next style="margin-top:10px;display:none">Next question</button>'+
      '<div class="exdone" data-done></div>');
    var qEl=b.querySelector('[data-q]'),opts=b.querySelector('[data-opts]'),fb=b.querySelector('[data-fb]'),
        nx=b.querySelector('[data-next]'),done=b.querySelector('[data-done]');
    function render(){answered=false;var q=qs[i];
      b.querySelector('[data-pos]').textContent='Question '+(i+1)+' of '+qs.length;
      b.querySelector('[data-score]').textContent=score+' correct';
      qEl.innerHTML=q.q;fb.className='ac-fb';fb.innerHTML='';nx.style.display='none';
      var shown=q._shown||(q._shown=shuffled(q.options));
      opts.innerHTML=shown.map(function(o,j){return '<button class="opt" data-j="'+j+'">'+o[0]+'</button>';}).join('');
      opts.querySelectorAll('.opt').forEach(function(btn){btn.addEventListener('click',function(){
        if(answered)return;answered=true;var j=+btn.dataset.j,right=!!shown[j][1];
        opts.querySelectorAll('.opt').forEach(function(x,k){if(shown[k][1])x.classList.add('right');});
        if(!right)btn.classList.add('wrong');else score++;
        b.querySelector('[data-score]').textContent=score+' correct';
        fb.className='ac-fb on '+(right?'ok':'no');
        fb.innerHTML=(right?'<b>Correct.</b> ':'<b>Not this one.</b> ')+(q.why||'');
        if(i<qs.length-1)nx.style.display='inline-block';else finish();});});}
    function finish(){var pct=Math.round(score/qs.length*100);
      done.className='exdone on '+(pct>=80?'g':(pct>=60?'a':'r'));
      done.innerHTML='<b>'+score+' of '+qs.length+' ('+pct+'%).</b> '+
        (pct>=80?'That is the range you want to be sitting in before you book the exam. Keep going on full-length timed sets rather than short ones, because the real challenge is concentration over four hours, not any single question.'
        :(pct>=60?'Passing territory on a good day, not on a bad one. Work out whether your misses cluster in one domain, because a pattern is much faster to fix than a scatter.'
        :'Not ready yet, and that is useful to know now rather than on exam day. Go back to the chapters behind your misses rather than doing more questions: more practice on shaky foundations mostly teaches you to be confidently wrong.'));}
    nx.addEventListener('click',function(){if(i<qs.length-1){i++;render();}});
    render();
  };

  R.tco=function(el){var c=cfgOf(el);var A=c.a||{},B=c.b||{},mn=c.minYears||5,mx=c.maxYears||50;
    function money(v){return v>=1000000?('$'+(v/1000000).toFixed(2)+'M'):('$'+Math.round(v/1000)+'k');}
    var b=shell(el,'<div class="pvrow"><span class="nm">Evaluate over</span><input type="range" min="'+mn+'" max="'+mx+'" step="1" value="'+(c.start||10)+'"><span class="v" data-y></span></div>'+
      '<div class="tcogrid">'+[A,B].map(function(o,i){
        return '<div class="tcocard" data-c="'+i+'"><div class="tt">'+o.name+'</div>'+
          '<div class="ln"><span>Build it</span><b>'+money(o.capital)+'</b></div>'+
          '<div class="ln"><span>Run it, each year</span><b>'+money(o.annual)+'</b></div>'+
          '<div class="tcobar"><i class="cap" data-cap="'+i+'"></i><i class="om" data-om="'+i+'"></i></div>'+
          '<div class="tot" data-t="'+i+'"></div><div class="win" data-w="'+i+'"></div></div>';}).join('')+'</div>'+
      '<div class="tconote" data-note></div>');
    var rng=b.querySelector('input');
    function upd(){var y=+rng.value;b.querySelector('[data-y]').textContent=y+' years';
      var tA=A.capital+A.annual*y,tB=B.capital+B.annual*y,mxT=Math.max(tA,tB);
      [[0,A,tA],[1,B,tB]].forEach(function(p){var i=p[0],o=p[1],t=p[2];
        b.querySelector('[data-cap="'+i+'"]').style.width=(o.capital/mxT*100)+'%';
        b.querySelector('[data-om="'+i+'"]').style.width=(o.annual*y/mxT*100)+'%';
        b.querySelector('[data-t="'+i+'"]').innerHTML='Total <b>'+money(t)+'</b>';});
      var aWins=tA<tB;
      b.querySelector('[data-w="0"]').textContent=aWins?'Cheaper':'';
      b.querySelector('[data-w="1"]').textContent=aWins?'':'Cheaper';
      b.querySelectorAll('.tcocard').forEach(function(x,i){x.classList.toggle('on',(i===0)===aWins);});
      var flip=Math.ceil((A.capital-B.capital)/(B.annual-A.annual));
      var note=b.querySelector('[data-note]');
      if(y<flip)note.innerHTML='At '+y+' years, <b>'+A.name+'</b> is cheaper, and this is the number that wins a bid opening. Keep dragging.';
      else note.innerHTML='At '+y+' years, <b>'+B.name+'</b> is cheaper. The two options cross at about <b>'+flip+' years</b>, and the asset will be in the ground for far longer than that. This is the whole argument for life-cycle costing: the option that wins on capital cost loses on ownership cost, and the utility lives with the ownership cost.';}
    rng.addEventListener('input',upd);upd();
  };

  R.firmcap=function(el){var c=cfgOf(el);var units=c.units||[];
    function u(v){return v+' '+(c.unit||'MGD');}
    var b=shell(el,'<div class="pvrow"><span class="nm">Peak day demand</span><input type="range" data-k="d" min="'+(c.minDemand||0)+'" max="'+(c.maxDemand||30)+'" step="'+(c.step||1)+'" value="'+(c.demand||18)+'"><span class="v" data-dv></span></div>'+
      '<label class="pschk fcchk"><input type="checkbox" data-k="out"><span>'+(c.outLabel||'Largest unit out of service')+'</span></label>'+
      '<div class="fcunits" data-units></div><div class="fcout" data-out></div><div class="fcnote" data-note></div>');
    var big=units.reduce(function(m,x){return x.capacity>m.capacity?x:m;},units[0]||{capacity:0});
    function upd(){var d=+b.querySelector('input[data-k="d"]').value,out=b.querySelector('input[data-k="out"]').checked;
      b.querySelector('[data-dv]').textContent=u(d);
      var avail=units.filter(function(x){return !(out&&x===big);});
      var total=units.reduce(function(s,x){return s+x.capacity;},0);
      var firm=avail.reduce(function(s,x){return s+x.capacity;},0);
      b.querySelector('[data-units]').innerHTML=units.map(function(x){var down=out&&x===big;
        return '<div class="fcunit'+(down?' down':'')+'"><span class="un">'+x.name+'</span><span class="uc">'+u(x.capacity)+'</span>'+(down?'<span class="ud">out</span>':'')+'</div>';}).join('');
      var ok=firm>=d,o=b.querySelector('[data-out]');
      o.className='fcout '+(ok?'g':'r');
      o.innerHTML='Installed capacity <b>'+u(total)+'</b>. '+(out?'Firm capacity <b>'+u(firm)+'</b>. ':'')+'Demand <b>'+u(d)+'</b>. '+(ok?'You can meet it.':'<b>You cannot meet it.</b>');
      b.querySelector('[data-note]').innerHTML=out
        ? (ok?'With your largest unit down you still cover demand. That is what <b>firm capacity</b> means, and it is the only capacity number worth planning against, because units go out of service for maintenance whether or not it is convenient.'
             :'This is the failure that matters. Installed capacity of '+u(total)+' looks comfortable against '+u(d)+', but with the largest unit out you are short. <b>Never size a system on installed capacity.</b> Size it on firm capacity, which is what you have on the day something is down, and something is always eventually down.')
        : 'Everything is running, so installed capacity is what you have and the numbers look fine. Now tick the box. The question a utility actually has to answer is not "can we meet demand today," it is "can we meet demand on the worst day with the biggest unit out."';}
    b.querySelectorAll('input').forEach(function(x){x.addEventListener('input',upd);x.addEventListener('change',upd);});upd();
  };

  R.controls=function(el){var c=cfgOf(el);var lv=c.levels||[];
    var b=shell(el,'<div class="hzq">'+(c.hazard||'')+'</div><div class="ctlad">'+lv.map(function(x,i){
        return '<button class="ctrow" data-i="'+i+'"><span class="rk">'+(i+1)+'</span><span class="cn"><b>'+x.name+'</b><em>'+(x.example||'')+'</em></span><span class="cr" data-r="'+i+'">'+x.residual+'</span></button>';}).join('')+'</div>'+
      '<div class="ctbarwrap"><div class="ctbar"><i data-bar></i></div><span class="ctval" data-val></span></div><div class="ctnote" data-note></div>');
    var note=b.querySelector('[data-note]'),bar=b.querySelector('[data-bar]'),val=b.querySelector('[data-val]');
    function pick(i){var x=lv[i];
      b.querySelectorAll('.ctrow').forEach(function(y){y.classList.remove('on');});
      b.querySelectorAll('.ctrow')[i].classList.add('on');
      bar.style.width=x.residual+'%';
      bar.className=x.residual<=20?'g':(x.residual<=55?'a':'r');
      val.textContent=x.residual+' of 100 risk remaining';
      note.innerHTML='<b>'+x.name+'.</b> '+(x.note||'');}
    b.querySelectorAll('.ctrow').forEach(function(y){y.addEventListener('click',function(){pick(+y.dataset.i);});});
    pick(c.start!=null?c.start:lv.length-1);
  };

  R.clearance=function(el){var c=cfgOf(el);var base=c.baseDays||6,perFail=c.failDays||4,planned=c.planned||2;
    var b=shell(el,'<div class="pvrow"><span class="nm">Sample rounds that fail</span><input type="range" min="0" max="3" step="1" value="0"><span class="v" data-n></span></div>'+
      '<div class="clsteps" data-steps></div><div class="clout" data-out></div><div class="clnote" data-note></div>');
    var rng=b.querySelector('input');
    function upd(){var f=+rng.value,total=base+f*perFail;
      b.querySelector('[data-n]').textContent=f===0?'none':(f+(f===1?' round':' rounds'));
      var steps=[];
      (c.steps||[]).forEach(function(s){steps.push({n:s.name,d:s.days,bad:false});});
      for(var i=0;i<f;i++){(c.retry||[]).forEach(function(s){steps.push({n:s.name+' (retry '+(i+1)+')',d:s.days,bad:true});});}
      b.querySelector('[data-steps]').innerHTML=steps.map(function(s){
        return '<div class="clrow'+(s.bad?' bad':'')+'"><span class="cs">'+s.n+'</span><span class="cd">'+s.d+(s.d===1?' day':' days')+'</span></div>';}).join('');
      var out=b.querySelector('[data-out]');
      out.className='clout '+(total<=planned+2?'g':(total<=planned+6?'a':'r'));
      out.innerHTML='<b>'+total+' days</b> from final weld to water in service. The bar chart on the schedule said <b>'+planned+' days</b>.';
      b.querySelector('[data-note]').innerHTML=f===0
        ? 'Even with everything passing first time, clearance takes <b>'+base+' days</b>, not the '+planned+' the schedule allowed. The hold time and the two samples taken 24 hours apart are fixed by the standard, and no amount of pressure changes them. This is why commissioning slips even on a job that built cleanly.'
        : 'One failed sample round does not cost you one day, it costs <b>'+perFail+'</b>, because you go back and repeat the whole flush, chlorinate, hold, and dechlorinate cycle before you can sample again. At '+f+(f===1?' failed round':' failed rounds')+' you are <b>'+(total-planned)+' days</b> past the plan, and this is the point in a project where people start being asked to put water in service before it has cleared.';}
    rng.addEventListener('input',upd);upd();
  };

  R.permitsim=function(el){var c=cfgOf(el);var attrs=c.attrs||[],permits=c.permits||[],dw=c.designWeeks||26;
    var b=shell(el,'<div class="psattrs">'+attrs.map(function(a,i){return '<label class="pschk"><input type="checkbox" data-k="'+a.key+'"'+(a.on?' checked':'')+'><span>'+a.label+'</span></label>';}).join('')+'</div>'+
      '<div class="pslist" data-list></div><div class="psout" data-out></div><div class="psnote" data-note></div>');
    var maxw=permits.reduce(function(m,p){return Math.max(m,p.weeks);},1);
    function upd(){var on={};b.querySelectorAll('input').forEach(function(x){on[x.dataset.k]=x.checked;});
      var act=permits.filter(function(p){var n=p.needs||[];if(!n.length)return true;return n.every(function(k){return on[k];});});
      act.sort(function(x,y){return y.weeks-x.weeks;});
      b.querySelector('[data-list]').innerHTML=act.length?act.map(function(p,i){
        return '<div class="psrow'+(i===0?' drives':'')+'"><span class="pn">'+p.name+'<em>'+p.agency+'</em></span><span class="pbar"><i style="width:'+Math.round(p.weeks/maxw*100)+'%"></i></span><span class="pw">'+p.weeks+' wk</span></div>'+
          (p.note?'<div class="psdesc">'+p.note+'</div>':'');}).join(''):'<div class="psdesc">No approvals triggered by these answers. That is rare on a utility job, and worth double checking.</div>';
      var lead=act.length?act[0]:null;
      var out=b.querySelector('[data-out]'),note=b.querySelector('[data-note]');
      if(!lead){out.className='psout';out.innerHTML='';note.innerHTML='';return;}
      var drives=lead.weeks>dw;
      out.className='psout '+(drives?'r':'g');
      out.innerHTML='Longest approval: <b>'+lead.weeks+' weeks</b> for the '+lead.name+'. Design and bid take about '+dw+' weeks.';
      note.innerHTML=drives
        ? 'At <b>'+lead.weeks+' weeks</b>, this approval is longer than the '+dw+' weeks of design and bid, so <b>permitting is on the critical path</b>. Nothing you do to speed up design will move the finish date. The only useful moves are starting the application earlier, filing while design is still at 60 percent, or changing the alignment so the approval is not triggered at all.'
        : 'The longest approval, <b>'+lead.weeks+' weeks</b>, fits inside the '+dw+' weeks of design and bid, so permitting rides along in parallel and does not drive the finish. Keep it that way by starting the application early. Approvals only become the critical path when you file them late.';}
    b.querySelectorAll('input').forEach(function(x){x.addEventListener('change',upd);});upd();
  };

  R.backplan=function(el){var c=cfgOf(el);var phases=c.phases||[];
    function pd(s){var p=String(s).split('-');return new Date(+p[0],+p[1]-1,+p[2]);}
    var dl=pd(c.deadline),today=pd(c.today);
    var MN=['January','February','March','April','May','June','July','August','September','October','November','December'];
    function fm(d){return MN[d.getMonth()]+' '+d.getFullYear();}
    var b=shell(el,phases.map(function(p){return '<div class="pvrow"><span class="nm">'+p.label+'</span><input type="range" data-k="'+p.key+'" min="'+p.min+'" max="'+p.max+'" step="1" value="'+p.months+'"><span class="v" data-v="'+p.key+'"></span></div>';}).join('')+
      '<div class="bpbar" data-bar></div><div class="bpout" data-out></div><div class="bpnote" data-note></div>');
    function upd(){var tot=0,vals={};
      phases.forEach(function(p){var v=+b.querySelector('input[data-k="'+p.key+'"]').value;vals[p.key]=v;tot+=v;
        b.querySelector('[data-v="'+p.key+'"]').textContent=v+' mo';});
      b.querySelector('[data-bar]').innerHTML=phases.map(function(p,i){
        return '<span class="bpseg s'+(i%4)+'" style="flex:'+vals[p.key]+'" data-lab="'+p.label+', '+vals[p.key]+' months">'+vals[p.key]+'</span>';}).join('');
      var start=new Date(dl.getFullYear(),dl.getMonth()-tot,dl.getDate());
      var slack=(start.getFullYear()-today.getFullYear())*12+(start.getMonth()-today.getMonth());
      var out=b.querySelector('[data-out]'),note=b.querySelector('[data-note]');
      out.className='bpout '+(slack<0?'r':(slack<=6?'a':'g'));
      out.innerHTML='<b>'+tot+' months</b> of work to deliver. To hit '+fm(dl)+', you must start by <b>'+fm(start)+'</b>.';
      if(slack<0)note.innerHTML='Today is '+fm(today)+'. That start date has <b>already passed by '+Math.abs(slack)+' months</b>. The deadline is not a planning target any more, it is a compliance problem, and the honest move is to say so now and ask for the compression money or the extension. Hoping the phases shrink is not a plan.';
      else if(slack<=6)note.innerHTML='Today is '+fm(today)+', which leaves <b>'+slack+' months</b> of cushion. That is thin for a capital job. One long permit or one failed bid opening eats it. Start the front end now.';
      else note.innerHTML='Today is '+fm(today)+', so you have <b>'+slack+' months</b> before the latest responsible start. Real room, but the point of a back plan is that it only stays real if you check it. Drag any phase longer and watch the cushion disappear.';}
    b.querySelectorAll('input').forEach(function(x){x.addEventListener('input',upd);});upd();
  };

  R.dashboard=function(el){var c=cfgOf(el);var metrics=c.metrics||[];
    function rag(m,v){return m.dir==='low'?(v<=m.amber?'g':(v<=m.red?'a':'r')):(v>=m.amber?'g':(v>=m.red?'a':'r'));}
    function fmt(m,v){return m.fmt==='int'?String(v):(+v).toFixed(2);}
    var b=shell(el,metrics.map(function(m){return '<div class="dashrow"><span class="nm">'+m.label+' <b data-v="'+m.key+'"></b></span><input type="range" data-k="'+m.key+'" min="'+m.min+'" max="'+m.max+'" step="'+m.step+'" value="'+m.value+'"><span class="rag" data-rag="'+m.key+'"></span></div>';}).join('')+
      '<div class="dashoverall" data-overall><div class="k">Honest overall status</div><div class="v" data-ov></div></div><div class="dashnote" data-note></div>');
    var labels={g:'On track',a:'Watch',r:'At risk'},words={g:'GREEN',a:'AMBER',r:'RED'};
    function upd(){var worst='g';
      metrics.forEach(function(m){var v=+b.querySelector('input[data-k="'+m.key+'"]').value,r=rag(m,v);
        b.querySelector('[data-v="'+m.key+'"]').textContent=fmt(m,v);
        var chip=b.querySelector('[data-rag="'+m.key+'"]');chip.className='rag '+r;chip.textContent=labels[r];
        if(r==='r')worst='r';else if(r==='a'&&worst!=='r')worst='a';});
      var ov=b.querySelector('[data-overall]');ov.className='dashoverall '+worst;b.querySelector('[data-ov]').textContent=words[worst];
      var note=b.querySelector('[data-note]');
      if(worst==='r')note.innerHTML='Honest status is <b>red</b>, because at least one measure is at risk. It does not matter that others are green: a status a board can act on takes the <b>worst</b> light, not the average. Reporting green here is the watermelon, green on the outside and red at the core.';
      else if(worst==='a')note.innerHTML='<b>Amber.</b> Something needs watching. Name it, say what you are doing about it, and do not let it drift to red unremarked.';
      else note.innerHTML='<b>Green, and genuinely so:</b> every measure is on track. Green should mean this, not "no bad news has reached me yet."';}
    b.querySelectorAll('input').forEach(function(x){x.addEventListener('input',upd);});upd();
  };

  R.coq=function(el){var c=cfgOf(el);var failBase=c.failBase||400,K=c.K||100,max=c.max||300,unit=c.unit||'k';
    function m(k){return '$'+Math.round(k)+unit;}
    var b=shell(el,'<div class="pvrow"><span class="nm">Prevention &amp; appraisal spend</span><input type="range" min="0" max="'+max+'" step="10" value="'+(c.start||40)+'"><span class="v" data-p></span></div>'+
      '<svg class="coqsvg" viewBox="0 0 300 150" data-svg></svg>'+
      '<div class="coqleg"><span><span class="sw" style="background:#0A78BA"></span>Prevention + appraisal</span><span><span class="sw" style="background:#D64545"></span>Failure cost</span><span><span class="sw" style="background:#0F1728"></span>Total</span></div>'+
      '<div class="coqout"><div class="o"><div class="k">Prevention</div><div class="val" data-vp></div></div><div class="o"><div class="k">Failure</div><div class="val" data-vf></div></div><div class="o key"><div class="k">Total quality cost</div><div class="val" data-vt></div></div></div>'+
      '<div class="coqnote" data-note></div>');
    var rng=b.querySelector('input');function failAt(p){return failBase*K/(K+p);}
    var optP=Math.max(0,Math.round(Math.sqrt(failBase*K)-K));
    function upd(){var p=+rng.value,f=failAt(p),t=p+f;
      b.querySelector('[data-p]').textContent=m(p);b.querySelector('[data-vp]').textContent=m(p);b.querySelector('[data-vf]').textContent=m(f);b.querySelector('[data-vt]').textContent=m(t);
      var x0=8,x1=292,y0=10,y1=128,xmax=max,ymax=failBase*1.05;function X(v){return x0+v/xmax*(x1-x0);}function Y(v){return y1-v/ymax*(y1-y0);}
      var pl='',fc='',tc='';for(var i=0;i<=40;i++){var pp=i/40*xmax;pl+=X(pp).toFixed(1)+','+Y(pp).toFixed(1)+' ';fc+=X(pp).toFixed(1)+','+Y(failAt(pp)).toFixed(1)+' ';tc+=X(pp).toFixed(1)+','+Y(pp+failAt(pp)).toFixed(1)+' ';}
      b.querySelector('[data-svg]').innerHTML='<polyline points="'+pl+'" fill="none" stroke="#0A78BA" stroke-width="1.5" opacity=".55"/>'+
        '<polyline points="'+fc+'" fill="none" stroke="#D64545" stroke-width="1.5" opacity=".55"/>'+
        '<polyline points="'+tc+'" fill="none" stroke="#0F1728" stroke-width="2.2"/>'+
        '<line x1="'+X(optP).toFixed(1)+'" y1="'+y0+'" x2="'+X(optP).toFixed(1)+'" y2="'+y1+'" stroke="#0E8A64" stroke-dasharray="3 3"/><text x="'+X(optP).toFixed(1)+'" y="8" text-anchor="middle" font-size="8" fill="#0E8A64">sweet spot</text>'+
        '<line x1="'+X(p).toFixed(1)+'" y1="'+y0+'" x2="'+X(p).toFixed(1)+'" y2="'+y1+'" stroke="#8595AB" stroke-dasharray="2 2"/>';
      var note=b.querySelector('[data-note]');
      if(p<optP-15){note.className='coqnote warn';note.innerHTML='<b>Under-investing.</b> Another dollar of prevention here still saves more than a dollar of failure. Catch problems earlier: better inspection, better specs, better training.';}
      else if(p>optP+15){note.className='coqnote warn';note.innerHTML='<b>Past the sweet spot.</b> More inspection now costs more than the failures it prevents. Quality has diminishing returns too.';}
      else{note.className='coqnote ok';note.innerHTML='<b>Near the sweet spot</b> (about '+m(optP)+'). Total cost of quality is close to its minimum: enough prevention to keep failures down, not so much you over-inspect.';}}
    rng.addEventListener('input',upd);upd();
  };

  R.grid=function(el){var c=cfgOf(el);var q=c.quadrants||{},items=c.items||[];
    var b=shell(el,'<div class="gridwrap"><div class="gridyax">'+(c.yLabel||'Impact')+'</div><div class="gridsq">'+
      '<div class="gridcell lo-hi"><span class="qlab">'+((q.tl&&q.tl.label)||'')+'</span></div>'+
      '<div class="gridcell hi-hi"><span class="qlab">'+((q.tr&&q.tr.label)||'')+'</span></div>'+
      '<div class="gridcell lo-lo"><span class="qlab">'+((q.bl&&q.bl.label)||'')+'</span></div>'+
      '<div class="gridcell hi-lo"><span class="qlab">'+((q.br&&q.br.label)||'')+'</span></div>'+
      items.map(function(it,i){return '<div class="griddot" data-i="'+i+'" style="left:'+it.x+'%;bottom:'+it.y+'%">'+(i+1)+'</div>';}).join('')+
      '</div><div class="gridxax">'+(c.xLabel||'Likelihood')+'</div></div>'+
      '<div style="font:600 12px var(--fm);color:var(--ink-2);margin:8px 0 0;display:flex;flex-wrap:wrap;gap:5px 14px">'+items.map(function(it,i){return '<span>'+(i+1)+'. '+it.name+'</span>';}).join('')+'</div>'+
      '<div class="griddetail" data-detail>Tap a numbered marker to read where it lands and what to do about it.</div>');
    var det=b.querySelector('[data-detail]');
    b.querySelectorAll('.griddot').forEach(function(d){d.addEventListener('click',function(){
      var it=items[+d.dataset.i],xh=it.x>=50,yh=it.y>=50,quad=yh?(xh?q.tr:q.tl):(xh?q.br:q.bl);
      b.querySelectorAll('.griddot').forEach(function(x){x.classList.remove('on');});d.classList.add('on');
      det.className='griddetail on';det.innerHTML='<b>'+it.name+'.</b> '+((quad&&quad.label)?'<b>'+quad.label+'</b>: ':'')+((quad&&quad.strategy)||'')+(it.note?' '+it.note:'');});});
  };

  R.channels=function(el){var c=cfgOf(el);var mn=c.min||2,mx=c.max||24;
    var b=shell(el,'<div class="pvrow"><span class="nm">Team size</span><input type="range" min="'+mn+'" max="'+mx+'" step="1" value="'+(c.start||6)+'"><span class="v" data-n></span></div>'+
      '<svg class="chsvg" viewBox="0 0 200 200" data-svg></svg><div class="chout" data-out></div><div class="chnote" data-note></div>');
    var rng=b.querySelector('input');
    function upd(){var n=+rng.value,ch=n*(n-1)/2;b.querySelector('[data-n]').textContent=n+' people';
      var cx=100,cy=100,r=80,pts=[];for(var i=0;i<n;i++){var a=-Math.PI/2+i/n*2*Math.PI;pts.push([cx+r*Math.cos(a),cy+r*Math.sin(a)]);}
      var lines='';for(var i2=0;i2<n;i2++)for(var j=i2+1;j<n;j++)lines+='<line x1="'+pts[i2][0].toFixed(1)+'" y1="'+pts[i2][1].toFixed(1)+'" x2="'+pts[j][0].toFixed(1)+'" y2="'+pts[j][1].toFixed(1)+'" stroke="#0A78BA" stroke-width="0.6" opacity="0.4"/>';
      var dots=pts.map(function(p){return '<circle cx="'+p[0].toFixed(1)+'" cy="'+p[1].toFixed(1)+'" r="5" fill="#0A78BA"/>';}).join('');
      b.querySelector('[data-svg]').innerHTML=lines+dots;
      b.querySelector('[data-out]').innerHTML='<b>'+ch+'</b> communication channels';
      b.querySelector('[data-note]').innerHTML='Channels grow as n(n-1)/2. Going from '+n+' to '+(n+1)+' people does not add one channel, it adds <b>'+n+'</b>. That is why large teams drown in communication, and why you structure it instead of letting everyone talk to everyone.';}
    rng.addEventListener('input',upd);upd();
  };

  R.zopa=function(el){var c=cfgOf(el);var mn=c.min||0,mx=c.max||100,unit=c.unit||'k',step=c.step||5;
    function m(v){return '$'+v+unit;}
    var b=shell(el,'<div class="pvrow"><span class="nm">Seller will not go below</span><input type="range" data-k="sell" min="'+mn+'" max="'+mx+'" step="'+step+'" value="'+(c.sell||60)+'"><span class="v" data-vsell></span></div>'+
      '<div class="pvrow"><span class="nm">Buyer will not go above</span><input type="range" data-k="buy" min="'+mn+'" max="'+mx+'" step="'+step+'" value="'+(c.buy||80)+'"><span class="v" data-vbuy></span></div>'+
      '<div class="zotrack" data-track></div><div class="zoout" data-out></div>');
    var isell=b.querySelector('[data-k=sell]'),ibuy=b.querySelector('[data-k=buy]');
    function X(v){return (v-mn)/(mx-mn)*100;}
    function upd(){var sell=+isell.value,buy=+ibuy.value;
      b.querySelector('[data-vsell]').textContent=m(sell);b.querySelector('[data-vbuy]').textContent=m(buy);
      var band='<div class="zoband sell" style="left:'+X(sell).toFixed(1)+'%;width:'+(100-X(sell)).toFixed(1)+'%"></div>'+
        '<div class="zoband buy" style="left:0;width:'+X(buy).toFixed(1)+'%"></div>';
      var out=b.querySelector('[data-out]');
      if(buy>=sell){band+='<div class="zozopa" style="left:'+X(sell).toFixed(1)+'%;width:'+(X(buy)-X(sell)).toFixed(1)+'%"></div>';
        out.className='zoout deal';out.innerHTML='Deal zone. Any price from <b>'+m(sell)+'</b> to <b>'+m(buy)+'</b> works for both. That overlap is the ZOPA, the zone of possible agreement ('+m(buy-sell)+' wide). Skilled negotiators find it, then split the difference.';}
      else{out.className='zoout nodeal';out.innerHTML='No deal. The seller floor ('+m(sell)+') is above the buyer ceiling ('+m(buy)+'), so there is <b>no overlap</b>. Someone must move their number, improve their alternative (BATNA), or walk away.';}
      b.querySelector('[data-track]').innerHTML=band;}
    isell.addEventListener('input',upd);ibuy.addEventListener('input',upd);upd();
  };

  R.contractrisk=function(el){var c=cfgOf(el);var target=c.target||1000,fee=c.fee||100,ffp=c.ffp||Math.round(target*1.10),gmpCap=c.gmpCap||Math.round(target*1.15);
    function m(k){return Math.abs(k)>=1000?'$'+(k/1000).toFixed(2)+'M':'$'+Math.round(k)+'k';}
    var b=shell(el,'<p style="font-size:14px;color:var(--ink-2);margin:0 0 8px">Estimated cost <b style="color:var(--ink)">'+m(target)+'</b>. Fixed price '+m(ffp)+', GMP cap '+m(gmpCap)+', fee '+m(fee)+'. Now move the actual cost the job really came in at.</p>'+
      '<div class="pvrow"><span class="nm">Final actual cost</span><input type="range" min="'+(c.min||Math.round(target*0.7))+'" max="'+(c.max||Math.round(target*1.5))+'" step="25" value="'+(c.start||Math.round(target*1.2))+'"><span class="v" data-a></span></div>'+
      '<div class="crcards" data-cards></div><div class="crnote" data-note></div>');
    var rng=b.querySelector('input');
    function upd(){var actual=+rng.value;b.querySelector('[data-a]').textContent=m(actual);
      var types=[
        {nm:'Firm Fixed Price',sub:'FFP: one price, no matter what',owner:ffp,cls:'contractor',who:'Contractor'},
        {nm:'Cost-plus / T&M',sub:'owner pays cost + a fee',owner:actual+fee,cls:'owner',who:'Owner'},
        {nm:'Guaranteed Max Price',sub:'GMP: owner pays cost + fee, capped',owner:Math.min(actual+fee,gmpCap),cls:'shared',who:'Shared'}
      ];
      b.querySelector('[data-cards]').innerHTML=types.map(function(t){var prof=t.owner-actual;
        return '<div class="crcard"><div class="nm">'+t.nm+'</div><div class="sub2">'+t.sub+'</div>'+
          '<div class="line"><span class="k">Owner pays</span><span class="v">'+m(t.owner)+'</span></div>'+
          '<div class="line"><span class="k">Contractor keeps</span><span class="v prof '+(prof>=0?'pos':'neg')+'">'+(prof>=0?'+':'')+m(prof)+'</span></div>'+
          '<div class="crexposed '+t.cls+'">'+t.who+' carries the risk</div></div>';}).join('');
      var over=actual>target,note=b.querySelector('[data-note]');
      if(actual>ffp)note.innerHTML='At <b>'+m(actual)+'</b> actual on a '+m(target)+' estimate, Fixed Price protects the owner (still '+m(ffp)+') while the contractor eats the '+m(actual-ffp)+' overrun. Cost-plus hands the whole overrun to the owner. GMP caps the owner at '+m(gmpCap)+' and the contractor covers the rest. <b>That risk transfer is exactly what you pay for in the price.</b>';
      else note.innerHTML='At <b>'+m(actual)+'</b>, under the fixed price, the Fixed Price contractor pockets the '+m(ffp-actual)+' saving, cost-plus passes the low cost straight to the owner, and GMP shares it. Push the actual above '+m(ffp)+' and watch who starts losing money.';}
    rng.addEventListener('input',upd);upd();
  };

  R.evm=function(el){var c=cfgOf(el);var bac=c.bac||1300;
    function m(k){return Math.abs(k)>=1000?'$'+(k/1000).toFixed(2)+'M':'$'+Math.round(k)+'k';}
    function row(k,label,sub,val,mn,mx,st){return '<div class="pvrow"><span class="nm">'+label+'<small style="display:block;font:11px var(--fm);color:var(--ink-3)">'+sub+'</small></span><input type="range" data-k="'+k+'" min="'+mn+'" max="'+mx+'" step="'+st+'" value="'+val+'"><span class="v" data-v="'+k+'"></span></div>';}
    var b=shell(el,
      '<p style="font-size:14px;color:var(--ink-2);margin:0 0 6px">Budget at completion (BAC): <b style="color:var(--ink)">'+m(bac)+'</b>. Now say where the job stands.</p>'+
      row('t','Schedule elapsed','how far through the planned time',c.t||50,0,100,5)+
      row('w','Work actually complete','percent of the job done',c.w||40,0,100,5)+
      row('a','Actual cost spent','dollars out the door so far',c.a||600,0,Math.round(bac*1.4),25)+
      '<svg class="evmsvg" viewBox="0 0 320 150" data-svg></svg>'+
      '<div class="evmleg"><span><span class="sw" style="background:#0A78BA"></span>Planned Value (PV)</span><span><span class="sw" style="background:#0E8A64"></span>Earned Value (EV)</span><span><span class="sw" style="background:#D64545"></span>Actual Cost (AC)</span></div>'+
      '<div class="evmstat"><div class="o"><div class="k">PV</div><div class="val" data-pv></div></div>'+
      '<div class="o"><div class="k">EV</div><div class="val" data-ev></div></div>'+
      '<div class="o"><div class="k">AC</div><div class="val" data-acost></div></div>'+
      '<div class="o" data-cpio><div class="k">CPI</div><div class="val" data-cpi></div></div>'+
      '<div class="o" data-spio><div class="k">SPI</div><div class="val" data-spi></div></div>'+
      '<div class="o key"><div class="k">Forecast (EAC)</div><div class="val" data-eac></div></div></div>'+
      '<div class="evmverdict" data-verdict></div>');
    function val(k){return +b.querySelector('input[data-k="'+k+'"]').value;}
    function ss(x){return x*x*(3-2*x);}
    function upd(){
      var t=val('t'),w=val('w'),ac=val('a');
      b.querySelector('[data-v="t"]').textContent=t+'%';b.querySelector('[data-v="w"]').textContent=w+'%';b.querySelector('[data-v="a"]').textContent=m(ac);
      var pv=bac*ss(t/100),ev=bac*w/100;
      var cpi=ac>0?ev/ac:0,spi=pv>0?ev/pv:0,eac=cpi>0?bac/cpi:bac;
      b.querySelector('[data-pv]').textContent=m(pv);b.querySelector('[data-ev]').textContent=m(ev);b.querySelector('[data-acost]').textContent=m(ac);
      b.querySelector('[data-cpi]').textContent=cpi.toFixed(2);b.querySelector('[data-spi]').textContent=spi.toFixed(2);b.querySelector('[data-eac]').textContent=m(eac);
      b.querySelector('[data-cpio]').className='o '+(cpi>=1?'good':'bad');b.querySelector('[data-spio]').className='o '+(spi>=1?'good':'bad');
      // chart
      var x0=8,x1=312,y0=10,y1=128,ymax=Math.max(bac,ac)*1.08||1;
      function X(f){return x0+f*(x1-x0);}function Y(v){return y1-v/ymax*(y1-y0);}
      var pvpts='';for(var i=0;i<=40;i++){var f=i/40;pvpts+=X(f).toFixed(1)+','+Y(bac*ss(f)).toFixed(1)+' ';}
      var tf=t/100;
      var svg='<polyline points="'+pvpts+'" fill="none" stroke="#0A78BA" stroke-width="1.6" opacity=".55"/>'+
        '<line x1="'+X(tf).toFixed(1)+'" y1="'+y0+'" x2="'+X(tf).toFixed(1)+'" y2="'+y1+'" stroke="#8595AB" stroke-dasharray="3 3"/>'+
        '<text x="'+X(tf).toFixed(1)+'" y="8" text-anchor="middle" font-size="8" fill="#8595AB">today</text>'+
        '<line x1="'+x0+'" y1="'+Y(0)+'" x2="'+X(tf).toFixed(1)+'" y2="'+Y(ev).toFixed(1)+'" stroke="#0E8A64" stroke-width="1.8"/>'+
        '<line x1="'+x0+'" y1="'+Y(0)+'" x2="'+X(tf).toFixed(1)+'" y2="'+Y(ac).toFixed(1)+'" stroke="#D64545" stroke-width="1.8"/>'+
        '<circle cx="'+X(tf).toFixed(1)+'" cy="'+Y(pv).toFixed(1)+'" r="3.4" fill="#0A78BA"/>'+
        '<circle cx="'+X(tf).toFixed(1)+'" cy="'+Y(ev).toFixed(1)+'" r="3.4" fill="#0E8A64"/>'+
        '<circle cx="'+X(tf).toFixed(1)+'" cy="'+Y(ac).toFixed(1)+'" r="3.4" fill="#D64545"/>'+
        '<line x1="'+x0+'" y1="'+y1+'" x2="'+x1+'" y2="'+y1+'" stroke="#CDD6E1"/>';
      b.querySelector('[data-svg]').innerHTML=svg;
      var v=b.querySelector('[data-verdict]'),over=cpi<1,behind=spi<1;
      var cls=(!over&&!behind)?'ok':((over&&behind)?'bad':'warn');
      var costTxt=cpi<1?'<b>over budget</b> (every dollar of work is costing '+(1/cpi).toFixed(2)+' dollars)':(cpi>1?'<b>under budget</b>':'right on budget');
      var schTxt=spi<1?'<b>behind schedule</b> (only '+(spi*100).toFixed(0)+' cents of work done per planned dollar)':(spi>1?'<b>ahead of schedule</b>':'on schedule');
      v.className='evmverdict '+cls;
      v.innerHTML='You are '+costTxt+' and '+schTxt+'. At this rate the job finishes near <b>'+m(eac)+'</b>'+(eac>bac?', about '+m(eac-bac)+' over the '+m(bac)+' budget.':(eac<bac?', under the '+m(bac)+' budget.':'.'))+' EAC = BAC / CPI: keep spending at today\'s efficiency and that is where you land.';
    }
    b.querySelectorAll('input').forEach(function(x){x.addEventListener('input',upd);});upd();
  };

  R.estrange=function(el){var c=cfgOf(el);var base=c.base||1300;
    var cls=c.classes||[
      {label:"Class 5 (Concept)",lo:-30,hi:50,note:"Order of magnitude, drawn on a napkin. Less than 2% design. Useful for a go / no-go, useless for a commitment."},
      {label:"Class 4 (Study)",lo:-20,hi:30,note:"Early feasibility, maybe 10% design. Good enough to compare options."},
      {label:"Class 3 (Budget)",lo:-15,hi:20,note:"Preliminary design, around 30%. This is the estimate you take to the board for budget authority."},
      {label:"Class 2 (Control)",lo:-10,hi:15,note:"Detailed design, 60 to 90%. Tight enough to control the project against."},
      {label:"Class 1 (Definitive)",lo:-5,hi:10,note:"Complete design, ready to bid. The narrowest range you will get before real bids come in."}
    ];
    function money(k){return Math.abs(k)>=1000?'$'+(k/1000).toFixed(2)+'M':'$'+Math.round(k)+'k';}
    var span=base*1.6;
    var b=shell(el,'<div class="pvrow"><span class="nm">Design maturity</span><input type="range" min="0" max="'+(cls.length-1)+'" step="1" value="0"><span class="v" data-cls></span></div>'+
      '<div class="ertrack" data-track></div>'+
      '<div class="erout"><div class="o lo"><div class="k">Low end</div><div class="val" data-lo></div></div>'+
      '<div class="o pt"><div class="k">Point estimate</div><div class="val">'+money(base)+'</div></div>'+
      '<div class="o hi2"><div class="k">High end</div><div class="val" data-hi></div></div></div>'+
      '<div class="ernote" data-note></div>');
    var rng=b.querySelector('input');
    function upd(){var i=+rng.value,cl=cls[i],lo=base*(1+cl.lo/100),hi=base*(1+cl.hi/100);
      b.querySelector('[data-cls]').textContent=cl.label;
      b.querySelector('[data-track]').innerHTML='<div class="erband" style="left:'+(lo/span*100).toFixed(1)+'%;width:'+((hi-lo)/span*100).toFixed(1)+'%"></div>'+
        '<div class="erpoint" style="left:'+(base/span*100).toFixed(1)+'%"><span>'+money(base)+'</span></div>';
      b.querySelector('[data-lo]').textContent=money(lo)+' ('+cl.lo+'%)';
      b.querySelector('[data-hi]').textContent=money(hi)+' (+'+cl.hi+'%)';
      b.querySelector('[data-note]').innerHTML='<b>'+cl.label+'.</b> '+cl.note+' The point estimate barely moves; what changes is how much you could be <b>wrong</b> by. Committing a budget on a Class 5 estimate is how projects blow up.';}
    rng.addEventListener('input',upd);upd();
  };

  R.cipplan=function(el){var c=cfgOf(el);var projects=c.projects||[];
    function money(k){return k>=1000?'$'+(k/1000).toFixed(1)+'M':'$'+k+'k';}
    var b=shell(el,'<div class="pvrow"><span class="nm">This year’s capital budget</span><input type="range" min="'+(c.min||1000)+'" max="'+(c.max||9000)+'" step="'+(c.step||250)+'" value="'+(c.start||4000)+'"><span class="v" data-cap></span></div>'+
      '<div class="cipsum"><span class="k">Funded this year</span><span class="v" data-sum></span></div><div data-list></div><div class="ernote" data-note></div>');
    var rng=b.querySelector('input');
    function upd(){var cap=+rng.value,spent=0,funded=0;
      b.querySelector('[data-cap]').textContent=money(cap);
      b.querySelector('[data-list]').innerHTML=projects.map(function(p){var fit=spent+p.cost<=cap;if(fit){spent+=p.cost;funded++;}
        return '<div class="ciprow '+(fit?'fund':'defer')+'"><span class="nm">'+p.name+'</span><span class="cost">'+money(p.cost)+'</span><span class="tag">'+(fit?'funded':'deferred')+'</span></div>';}).join('');
      b.querySelector('[data-sum]').textContent=money(spent)+' of '+money(cap);
      var deferred=projects.length-funded;
      b.querySelector('[data-note]').innerHTML=deferred>0?'<b>'+funded+' funded, '+deferred+' deferred</b> to a later year. A CIP is a queue: you fund the top priorities each year and the rest wait their turn. Raise the budget and more fit, but that money has to come from rates, debt, or grants, which is the next section.':'Everything fits this year. Most utilities are not so lucky and spread projects across the multi-year plan.';}
    rng.addEventListener('input',upd);upd();
  };

  R.rateimpact=function(el){var c=cfgOf(el);
    function row(k,label,sub,val,mn,mx,st){return '<div class="pvrow"><span class="nm">'+label+'<small style="display:block;font:11px var(--fm);color:var(--ink-3)">'+sub+'</small></span><input type="range" data-k="'+k+'" min="'+mn+'" max="'+mx+'" step="'+st+'" value="'+val+'"><span class="v" data-v="'+k+'"></span></div>';}
    var b=shell(el,
      row('cost','Project cost','up-front dollars',c.cost||1300,200,4000,50)+
      row('debt','Share funded by debt','the rest is cash or grants',c.debt||80,0,100,5)+
      row('rate','Interest rate','SRF is far below market',c.rate||4,1,8,0.25)+
      row('term','Loan term','years',c.term||20,5,40,1)+
      row('acct','Customer accounts','thousands of bills',c.acct||15,1,120,1)+
      '<div class="riout"><div class="o"><div class="k">Debt service / year</div><div class="val" data-ds></div></div>'+
      '<div class="o"><div class="k">Per account / year</div><div class="val" data-yr></div></div>'+
      '<div class="o big"><div class="k">Per account / month</div><div class="val" data-mo></div></div></div>'+
      '<div class="rinote" data-note></div>');
    function val(k){return +b.querySelector('input[data-k="'+k+'"]').value;}
    function money(k){return Math.abs(k)>=1000?'$'+(k/1000).toFixed(2)+'M':'$'+Math.round(k)+'k';}
    function upd(){
      var cost=val('cost'),debtPct=val('debt'),rate=val('rate'),term=val('term'),acct=val('acct');
      b.querySelector('[data-v="cost"]').textContent=money(cost);b.querySelector('[data-v="debt"]').textContent=debtPct+'%';
      b.querySelector('[data-v="rate"]').textContent=rate.toFixed(2)+'%';b.querySelector('[data-v="term"]').textContent=term+' yr';b.querySelector('[data-v="acct"]').textContent=acct+'k';
      var debt=cost*debtPct/100,r=rate/100;
      var ds=r>0?debt*(r*Math.pow(1+r,term))/(Math.pow(1+r,term)-1):debt/term; // annual debt service, $k
      var perYr=ds/acct;            // $k / (k accounts) = dollars per account per year
      var perMo=perYr/12;
      b.querySelector('[data-ds]').textContent=money(ds)+'/yr';
      b.querySelector('[data-yr]').textContent='$'+perYr.toFixed(2);
      b.querySelector('[data-mo]').textContent='$'+perMo.toFixed(2);
      b.querySelector('[data-note]').innerHTML='This one project adds about <b>$'+perMo.toFixed(2)+' a month</b> to the average bill. Small on its own, but a utility runs many at once, and the whole capital plan stacked together is what actually moves the rate. This per-bill number is what a board and the public really ask about.';}
    b.querySelectorAll('input').forEach(function(x){x.addEventListener('input',upd);});upd();
  };

  R.pert=function(el){var c=cfgOf(el);var unit=c.unit||'days',mn=c.min||1,mx=c.max||30;
    var b=shell(el,
      '<div class="pertrow"><span class="nm">Optimistic<small>best case</small></span><input type="range" data-k="o" min="'+mn+'" max="'+mx+'" step="1" value="'+(c.o||4)+'"><span class="v" data-vo></span></div>'+
      '<div class="pertrow"><span class="nm">Most likely<small>your gut guess</small></span><input type="range" data-k="m" min="'+mn+'" max="'+mx+'" step="1" value="'+(c.m||6)+'"><span class="v" data-vm></span></div>'+
      '<div class="pertrow"><span class="nm">Pessimistic<small>worst case</small></span><input type="range" data-k="p" min="'+mn+'" max="'+mx+'" step="1" value="'+(c.p||14)+'"><span class="v" data-vp></span></div>'+
      '<svg class="pertsvg" viewBox="0 0 300 120" data-svg></svg>'+
      '<div class="pertout"><div class="o"><div class="k">Most likely</div><div class="val" data-ml></div></div>'+
      '<div class="o hi"><div class="k">PERT expected</div><div class="val" data-ex></div></div>'+
      '<div class="o"><div class="k">Std deviation</div><div class="val" data-sd></div></div></div>'+
      '<div class="rlnote" data-note style="margin-top:12px"></div>');
    var io=b.querySelector('[data-k=o]'),im=b.querySelector('[data-k=m]'),ip=b.querySelector('[data-k=p]');
    function upd(src){var o=+io.value,m=+im.value,p=+ip.value;
      if(src==='o'&&o>m){m=o;im.value=m;}if(src==='p'&&p<m){m=p;im.value=m;}
      if(src==='m'){if(m<o){o=m;io.value=o;}if(m>p){p=m;ip.value=p;}}if(o>p){p=o;ip.value=p;}
      b.querySelector('[data-vo]').textContent=o+' '+unit;b.querySelector('[data-vm]').textContent=m+' '+unit;b.querySelector('[data-vp]').textContent=p+' '+unit;
      var ex=(o+4*m+p)/6,sd=(p-o)/6;
      b.querySelector('[data-ml]').textContent=m+' '+unit;b.querySelector('[data-ex]').textContent=(Math.round(ex*10)/10)+' '+unit;b.querySelector('[data-sd]').textContent='±'+(Math.round(sd*10)/10);
      var y0=10,y1=104,x0=10,x1=290,rng=(p-o)||1;function X(v){return x0+(v-o)/rng*(x1-x0);}
      b.querySelector('[data-svg]').innerHTML=
        '<polygon points="'+X(o)+','+y1+' '+X(m)+','+y0+' '+X(p)+','+y1+'" fill="rgba(10,120,186,.12)" stroke="#0A78BA" stroke-width="2"/>'+
        '<line x1="'+X(m)+'" y1="'+y0+'" x2="'+X(m)+'" y2="'+y1+'" stroke="#8595AB" stroke-dasharray="3 3"/>'+
        '<line x1="'+X(ex)+'" y1="18" x2="'+X(ex)+'" y2="'+y1+'" stroke="#A97B0F" stroke-width="2"/>'+
        '<text x="'+X(ex)+'" y="14" text-anchor="middle" font-size="9" fill="#A97B0F" font-weight="700">expected</text>'+
        '<text x="'+X(o)+'" y="118" font-size="8" fill="#8595AB">'+o+'</text><text x="'+X(p)+'" y="118" text-anchor="end" font-size="8" fill="#8595AB">'+p+'</text>';
      b.querySelector('[data-note]').innerHTML='PERT weights the most likely four times, then averages it with the two extremes: (O + 4M + P) / 6. When the worst case has a long tail, the expected value lands to the <b>right</b> of your gut guess. That gap is why single-point estimates run optimistic.';}
    io.addEventListener('input',function(){upd('o');});im.addEventListener('input',function(){upd('m');});ip.addEventListener('input',function(){upd('p');});upd();
  };

  R.reslevel=function(el){var c=cfgOf(el);var cap=c.cap||3,unit=c.unit||'crews',states={before:c.before||{},after:c.after||{}},cur='before';
    var b=shell(el,'<div class="rltoggle"><button data-s="before" class="on">Before leveling</button><button data-s="after">After leveling</button></div>'+
      '<div class="rlwrap"><div class="rlbars" data-bars></div></div><div class="rllabels" data-labels></div><div class="rlnote" data-note></div>');
    var colors=['#0A78BA','#3E9BD6','#8FC4E8','#A97B0F','#C7A24E'];
    function draw(){var st=states[cur],W=st.weeks||6,load=[],segs=[];
      for(var w=0;w<W;w++){load[w]=0;segs[w]=[];}
      (st.tasks||[]).forEach(function(t,ti){for(var w2=t.start;w2<t.start+t.dur;w2++){load[w2]=(load[w2]||0)+t.crew;segs[w2].push({crew:t.crew,ti:ti});}});
      var maxLoad=Math.max(cap+1,Math.max.apply(null,load));
      b.querySelector('[data-bars]').innerHTML='<div class="rlcap" style="bottom:'+(cap/maxLoad*100).toFixed(1)+'%"><span>cap '+cap+'</span></div>'+
        load.map(function(l,w){var over=l>cap;return '<div class="rlcol">'+segs[w].map(function(s){return '<div class="rlseg'+(over?' rlover':'')+'" style="height:'+(s.crew/maxLoad*100).toFixed(1)+'%;background:'+colors[s.ti%colors.length]+'"></div>';}).join('')+'</div>';}).join('');
      b.querySelector('[data-labels]').innerHTML=load.map(function(l,w){return '<span>w'+(w+1)+'</span>';}).join('');
      var note=b.querySelector('[data-note]');
      if(cur==='before'){note.className='rlnote warn';note.innerHTML='Over-allocated. Some weeks poke above the <b>cap of '+cap+' '+unit+'</b> (red outline). You have promised more crews than exist. The bar chart looks fine, but this schedule cannot actually be staffed.';}
      else{note.className='rlnote ok';note.innerHTML='Leveled. Work was shifted so no week exceeds the cap, at the cost of a <b>longer finish</b> ('+(st.weeks)+' weeks instead of '+(states.before.weeks)+'). Leveling trades schedule length for a plan you can staff. Smoothing does the same but only uses existing float, so it does not push the finish.';}}
    b.querySelectorAll('.rltoggle button').forEach(function(btn){btn.addEventListener('click',function(){cur=btn.dataset.s;b.querySelectorAll('.rltoggle button').forEach(function(x){x.classList.toggle('on',x===btn);});draw();});});
    draw();
  };

  R.montecarlo=function(el){var c=cfgOf(el);var unit=c.unit||'weeks',iters=c.iterations||1000,tasks=c.tasks||[];
    function deps(t){return (t.deps||[]).map(function(d){return typeof d==='object'?(d.to||d.id):d;});}
    function finish(durs){var EF={};tasks.forEach(function(t){EF[t.id]=durs[t.id];});
      for(var i=0;i<tasks.length+1;i++)tasks.forEach(function(t){var es=0;deps(t).forEach(function(id){es=Math.max(es,EF[id]);});EF[t.id]=es+durs[t.id];});
      var mx=0;tasks.forEach(function(t){mx=Math.max(mx,EF[t.id]);});return mx;}
    function tri(o,m,p){var u=Math.random(),cc=(m-o)/((p-o)||1);return u<cc?o+Math.sqrt(u*(p-o)*(m-o)):p-Math.sqrt((1-u)*(p-o)*(p-m));}
    var detDur={};tasks.forEach(function(t){detDur[t.id]=t.m;});var det=finish(detDur);
    var b=shell(el,'<svg class="mcsvg" viewBox="0 0 320 150" data-svg></svg>'+
      '<div class="mcctrl"><button class="primary" data-run>&#9654; Run 1,000 simulations</button><button data-reset>Reset</button><span class="mccount" data-count></span></div>'+
      '<div class="mcstats"><div class="o det"><div class="k">Plan (most likely)</div><div class="val">'+Math.round(det)+' '+unit+'</div></div>'+
      '<div class="o p50"><div class="k">P50 (coin flip)</div><div class="val" data-p50>-</div></div>'+
      '<div class="o p80"><div class="k">P80 (safe commit)</div><div class="val" data-p80>-</div></div></div>'+
      '<div class="mcout" data-out>Press Run. Each simulation rolls a realistic duration for every task from its range and finds the finish date. Do it a thousand times and you get the odds, not a single guess.</div>');
    var results=[],timer=null,svg=b.querySelector('[data-svg]'),cnt=b.querySelector('[data-count]');
    function pctile(arr,q){var s=arr.slice().sort(function(a,bb){return a-bb;});return s[Math.min(s.length-1,Math.floor(q*s.length))];}
    function draw(){if(!results.length){svg.innerHTML='';return;}
      var mn=Math.min.apply(null,results),mx=Math.max.apply(null,results),lo=Math.floor(Math.min(mn,det)),hi=Math.ceil(mx),nb=Math.max(6,Math.min(26,hi-lo+1)),bins=[];
      for(var i=0;i<nb;i++)bins[i]=0;var bw=(hi-lo)/nb||1;
      results.forEach(function(v){bins[Math.min(nb-1,Math.floor((v-lo)/bw))]++;});
      var maxB=Math.max.apply(null,bins)||1,x0=8,x1=312,y0=10,y1=120;function X(v){return x0+(v-lo)/((hi-lo)||1)*(x1-x0);}
      var bars=bins.map(function(cn,i){var bx=x0+i/nb*(x1-x0),bwid=(x1-x0)/nb-1,bh=cn/maxB*(y1-y0);return '<rect x="'+bx.toFixed(1)+'" y="'+(y1-bh).toFixed(1)+'" width="'+bwid.toFixed(1)+'" height="'+bh.toFixed(1)+'" fill="#D3EAF8"/>';}).join('');
      var p50=pctile(results,0.5),p80=pctile(results,0.8);
      function mk(v,col,lab,yl){return '<line x1="'+X(v).toFixed(1)+'" y1="'+y0+'" x2="'+X(v).toFixed(1)+'" y2="'+y1+'" stroke="'+col+'" stroke-width="2"/><text x="'+X(v).toFixed(1)+'" y="'+yl+'" text-anchor="middle" font-size="8" fill="'+col+'" font-weight="700">'+lab+'</text>';}
      svg.innerHTML=bars+mk(det,'#8595AB','plan',8)+mk(p50,'#0A78BA','P50',18)+mk(p80,'#A97B0F','P80',28)+
        '<line x1="'+x0+'" y1="'+y1+'" x2="'+x1+'" y2="'+y1+'" stroke="#CDD6E1"/>'+
        '<text x="'+x0+'" y="148" font-size="8" fill="#8595AB">'+lo+' '+unit+'</text><text x="'+x1+'" y="148" text-anchor="end" font-size="8" fill="#8595AB">'+hi+' '+unit+'</text>';
      b.querySelector('[data-p50]').textContent=Math.round(p50)+' '+unit;b.querySelector('[data-p80]').textContent=Math.round(p80)+' '+unit;
      var beat=results.filter(function(v){return v<=det;}).length/results.length*100;
      b.querySelector('[data-out]').innerHTML='The plan says <b>'+Math.round(det)+' '+unit+'</b>, but only about <b>'+Math.round(beat)+'%</b> of runs actually finish that fast. Half come in by <b>'+Math.round(p50)+'</b>, and to be roughly 80% safe you commit to <span class="g">'+Math.round(p80)+' '+unit+'</span>. The gap between the plan and P80 is your real schedule risk.';}
    function reset(){if(timer){clearInterval(timer);timer=null;}results=[];cnt.textContent='';svg.innerHTML='';b.querySelector('[data-p50]').textContent='-';b.querySelector('[data-p80]').textContent='-';b.querySelector('[data-run]').disabled=false;}
    b.querySelector('[data-run]').addEventListener('click',function(){reset();var done=0;b.querySelector('[data-run]').disabled=true;
      timer=setInterval(function(){for(var k=0;k<40&&done<iters;k++){var durs={};tasks.forEach(function(t){durs[t.id]=tri(t.o,t.m,t.p);});results.push(finish(durs));done++;}
        cnt.textContent=done+' / '+iters;draw();if(done>=iters){clearInterval(timer);timer=null;b.querySelector('[data-run]').disabled=false;b.querySelector('[data-run]').innerHTML='&#9654; Run again';}},30);});
    b.querySelector('[data-reset]').addEventListener('click',function(){reset();b.querySelector('[data-out]').innerHTML='Reset. Press Run to simulate again.';b.querySelector('[data-run]').innerHTML='&#9654; Run 1,000 simulations';});
  };

  R.provnet=function(el){var c=cfgOf(el),nodes=c.nodes||[],edges=c.edges||[],steps=c.steps||[],cur=0,timer=null;
    var b=shell(el,'<div class="pnstage"><svg viewBox="0 0 760 330" role="img" aria-label="'+(c.ariaLabel||'Provenance network')+'" data-svg></svg></div><div class="pnkey"><span><i class="entity"></i>Entity or record</span><span><i class="activity"></i>Activity</span><span><i class="agent"></i>Agent</span></div><div class="pnctrl"><button data-action="reset">Reset</button><button data-action="back">Back</button><button class="primary" data-action="step">Step</button><button data-action="play">Play</button><span data-count></span></div><div class="pnnarr" data-narr aria-live="polite"></div>');
    var svg=b.querySelector('[data-svg]'),narr=b.querySelector('[data-narr]'),count=b.querySelector('[data-count]');
    function stop(){if(timer){clearInterval(timer);timer=null;}b.querySelector('[data-action="play"]').textContent='Play';}
    function color(kind){return kind==='activity'?'#A97B0F':kind==='agent'?'#0E8A64':'#0A78BA';}
    function paint(){var step=steps[cur]||{focus:[],title:'Network',body:''},focus=step.focus||[];
      var edgeHtml=edges.map(function(edge){var a=nodes.find(function(n){return n.id===edge.from;}),z=nodes.find(function(n){return n.id===edge.to;});if(!a||!z)return '';
        var active=focus.includes(edge.from)&&focus.includes(edge.to);var mx=(a.x+z.x)/2,my=(a.y+z.y)/2;
        return '<g class="pnedge'+(active?' on':'')+'"><line x1="'+a.x+'" y1="'+a.y+'" x2="'+z.x+'" y2="'+z.y+'" marker-end="url(#pn-arrow)"/><text x="'+mx+'" y="'+(my-7)+'">'+(edge.label||'')+'</text></g>';}).join('');
      var nodeHtml=nodes.map(function(node){var active=focus.includes(node.id),w=node.w||142,h=node.h||58,x=node.x-w/2,y=node.y-h/2;
        return '<g class="pnnode '+(node.kind||'entity')+(active?' on':'')+'" transform="translate('+x+' '+y+')"><rect width="'+w+'" height="'+h+'" rx="12"/><circle cx="17" cy="17" r="6" fill="'+color(node.kind)+'"/><text class="main" x="'+(w/2)+'" y="'+(h/2-2)+'">'+node.label+'</text><text class="sub" x="'+(w/2)+'" y="'+(h/2+16)+'">'+(node.sub||'')+'</text></g>';}).join('');
      svg.innerHTML='<defs><marker id="pn-arrow" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#8595AB"/></marker></defs>'+edgeHtml+nodeHtml;
      narr.innerHTML='<b>'+((cur+1)+'. '+(step.title||'Follow the evidence'))+'</b> '+(step.body||'');count.textContent=(cur+1)+' / '+Math.max(steps.length,1);
      b.querySelector('[data-action="back"]').disabled=cur===0;b.querySelector('[data-action="step"]').disabled=cur>=steps.length-1;
    }
    function advance(){if(cur<steps.length-1){cur++;paint();}else stop();}
    b.querySelector('[data-action="reset"]').addEventListener('click',function(){stop();cur=0;paint();});
    b.querySelector('[data-action="back"]').addEventListener('click',function(){stop();if(cur>0)cur--;paint();});
    b.querySelector('[data-action="step"]').addEventListener('click',function(){stop();advance();});
    b.querySelector('[data-action="play"]').addEventListener('click',function(){if(timer){stop();return;}if(cur>=steps.length-1){cur=0;paint();}this.textContent='Pause';advance();timer=setInterval(advance,1800);});paint();
  };

  R.qualityfit=function(el){var c=cfgOf(el),dims=c.dimensions||[],uses=c.uses||[];
    var options=uses.map(function(use,i){return '<option value="'+i+'">'+use.label+'</option>';}).join('');
    var rows=dims.map(function(dim){return '<label class="qfrow"><span><b>'+dim.label+'</b><small>'+(dim.help||'')+'</small></span><input type="range" min="0" max="100" step="1" value="'+(dim.value==null?80:dim.value)+'" data-id="'+dim.id+'" aria-label="'+dim.label+' evidence level"><output data-value="'+dim.id+'"></output><div class="qftrack"><i data-fill="'+dim.id+'"></i><em data-gate="'+dim.id+'"></em></div><strong data-state="'+dim.id+'"></strong></label>';}).join('');
    var b=shell(el,'<div class="qfuse"><label>Intended use<select data-use>'+options+'</select></label><p data-use-note></p></div><div class="qfrows">'+rows+'</div><div class="qfverdict" data-verdict aria-live="polite"></div><div class="qfboundary">'+(c.boundary||'This teaching model compares stated evidence with stated use thresholds. It is not a certified data-quality score or a compliance conclusion.')+'</div>');
    function val(id){return +b.querySelector('input[data-id="'+id+'"]').value;}
    function paint(){var use=uses[+b.querySelector('[data-use]').value]||{required:{},label:'this use'},failed=[];
      dims.forEach(function(dim){var current=val(dim.id),required=(use.required||{})[dim.id]||0,ok=current>=required;
        b.querySelector('[data-value="'+dim.id+'"]').textContent=current+' / 100';b.querySelector('[data-fill="'+dim.id+'"]').style.width=current+'%';b.querySelector('[data-gate="'+dim.id+'"]').style.left=required+'%';
        var state=b.querySelector('[data-state="'+dim.id+'"]');state.className=ok?'pass':'fail';state.textContent=ok?'Meets '+required:'Needs '+required;if(!ok)failed.push(dim.label);
      });
      b.querySelector('[data-use-note]').textContent=use.note||'';var verdict=b.querySelector('[data-verdict]');
      if(failed.length){verdict.className='qfverdict fail';verdict.innerHTML='<b>Not fit for '+use.label+'.</b> The stated evidence does not yet meet: '+failed.join(', ')+'. '+(use.consequence||'Resolve the gap or change the intended use.');}
      else{verdict.className='qfverdict pass';verdict.innerHTML='<b>Fit for the stated use in this exercise.</b> Every required dimension meets its threshold. Retain the evidence, approval, use limits, and review date. This result does not transfer automatically to another use.';}
    }
    b.querySelector('[data-use]').addEventListener('change',paint);b.querySelectorAll('input[type="range"]').forEach(function(input){input.addEventListener('input',paint);});paint();
  };

  R.applicability=function(el){var c=cfgOf(el),scenarios=c.scenarios||[],selected=0,gate=-1;
    var tabs=scenarios.map(function(s,i){return '<button data-s="'+i+'"'+(i===0?' class="on"':'')+'>'+s.label+'</button>';}).join('');
    var b=shell(el,'<div class="aptabs">'+tabs+'</div><div class="apcase" data-case></div><div class="apgates" data-gates></div><div class="apctrl"><button data-reset>Reset</button><button class="primary" data-run>Run next gate</button><span data-count></span></div><div class="apresult" data-result aria-live="polite"></div><div class="apboundary">'+(c.boundary||'This teaching tool structures an applicability review. It does not make a legal conclusion. Use the current controlled source, facts, authorized legal or regulatory reviewer, and retained evidence.')+'</div>');
    function stateLabel(state){return state==='pass'?'supported':state==='fail'?'not supported':'review needed';}
    function paint(){var s=scenarios[selected]||{gates:[]},g=s.gates||[];
      b.querySelector('[data-case]').innerHTML='<b>'+s.authority+'</b><span>'+(s.facts||'')+'</span>';
      b.querySelector('[data-gates]').innerHTML=g.map(function(x,i){var seen=i<=gate,active=i===gate;return '<article class="apgate '+(seen?(x.state||'review'):'pending')+(active?' active':'')+'"><i>'+(i+1)+'</i><div><b>'+x.label+'</b><span>'+(seen?x.detail:'Run the gate to examine this fact.')+'</span></div><em>'+(seen?stateLabel(x.state):'pending')+'</em></article>';}).join('');
      var complete=gate>=g.length-1&&g.length;b.querySelector('[data-count]').textContent=Math.max(0,gate+1)+' / '+g.length;b.querySelector('[data-run]').disabled=complete;
      var out=b.querySelector('[data-result]');if(complete){out.className='apresult '+(s.resultClass||'review');out.innerHTML='<b>'+s.result+'</b> '+s.basis;}else{out.className='apresult';out.textContent='Run every gate before recording an applicability decision.';}
    }
    b.querySelectorAll('[data-s]').forEach(function(btn){btn.addEventListener('click',function(){selected=+btn.dataset.s;gate=-1;b.querySelectorAll('[data-s]').forEach(function(x){x.classList.toggle('on',x===btn);});paint();});});
    b.querySelector('[data-run]').addEventListener('click',function(){var g=(scenarios[selected]||{gates:[]}).gates||[];if(gate<g.length-1)gate++;paint();});
    b.querySelector('[data-reset]').addEventListener('click',function(){gate=-1;paint();});paint();
  };

  R.estatemap=function(el){var c=cfgOf(el),nodes=c.nodes||[],edges=c.edges||[],views=c.views||[{label:'Whole estate',focus:[]}],selected=0;
    var legend=(c.legend||[]).map(function(x){return '<span><i style="background:'+x.color+'"></i>'+x.label+'</span>';}).join('');
    var tabs=views.map(function(v,i){return '<button data-v="'+i+'"'+(i===0?' class="on"':'')+'>'+v.label+'</button>';}).join('');
    var b=shell(el,'<div class="emtabs">'+tabs+'</div><div class="emstage"><svg viewBox="0 0 780 390" role="img" aria-label="'+(c.ariaLabel||'Utility data estate map')+'" data-svg></svg></div><div class="emlegend">'+legend+'</div><div class="emnarr" data-narr aria-live="polite"></div>');
    function color(kind){var found=(c.legend||[]).find(function(x){return x.kind===kind;});return found?found.color:'#0A78BA';}
    function paint(){var view=views[selected]||{focus:[]},focus=view.focus||[],all=!focus.length;
      var edgeHtml=edges.map(function(e){var a=nodes.find(function(n){return n.id===e.from;}),z=nodes.find(function(n){return n.id===e.to;});if(!a||!z)return '';var on=all||(focus.includes(e.from)&&focus.includes(e.to));return '<g class="emedge'+(on?' on':'')+'"><line x1="'+a.x+'" y1="'+a.y+'" x2="'+z.x+'" y2="'+z.y+'" marker-end="url(#em-arrow)"/><text x="'+((a.x+z.x)/2)+'" y="'+(((a.y+z.y)/2)-6)+'">'+(e.label||'')+'</text></g>';}).join('');
      var nodeHtml=nodes.map(function(n){var on=all||focus.includes(n.id),w=n.w||136,h=n.h||58;return '<g class="emnode'+(on?' on':'')+'" transform="translate('+(n.x-w/2)+' '+(n.y-h/2)+')"><rect width="'+w+'" height="'+h+'" rx="12"/><circle cx="16" cy="16" r="6" fill="'+color(n.kind)+'"/><text class="main" x="'+(w/2)+'" y="'+(h/2-2)+'">'+n.label+'</text><text class="sub" x="'+(w/2)+'" y="'+(h/2+15)+'">'+(n.sub||'')+'</text></g>';}).join('');
      b.querySelector('[data-svg]').innerHTML='<defs><marker id="em-arrow" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#8595AB"/></marker></defs>'+edgeHtml+nodeHtml;
      b.querySelector('[data-narr]').innerHTML='<b>'+view.label+'.</b> '+(view.body||'Every material system, file, service, interface, supplier, and manual step should connect to the decision it supports.');
    }
    b.querySelectorAll('[data-v]').forEach(function(btn){btn.addEventListener('click',function(){selected=+btn.dataset.v;b.querySelectorAll('[data-v]').forEach(function(x){x.classList.toggle('on',x===btn);});paint();});});paint();
  };

  R.identitybridge=function(el){var c=cfgOf(el),records=c.records||[],stage=0;
    var b=shell(el,'<div class="ibcanonical"><span>Governed identity</span><b>'+(c.canonical||'Canonical asset identifier')+'</b><small>'+(c.canonicalDetail||'One controlled identity, not one replacement system')+'</small></div><div class="ibrecords" data-records></div><div class="ibctrl"><button data-reset>Reset</button><button class="primary" data-step>Run next control</button><span data-count></span></div><div class="ibmetrics"><article><b data-match>0%</b><span>controlled match rate</span></article><article><b data-ex>0</b><span>exceptions queued</span></article><article><b data-guess>0</b><span>guesses accepted</span></article></div><div class="ibnarr" data-narr aria-live="polite"></div>');
    function status(r){if(stage===0)return 'raw';if(r.status==='exact')return 'matched';if(stage>=2&&r.status==='mapped')return 'matched';if(stage>=3&&(r.status==='conflict'||r.status==='nickname'))return 'exception';return 'pending';}
    function paint(){var matched=0,exceptions=0;
      b.querySelector('[data-records]').innerHTML=records.map(function(r){var s=status(r);if(s==='matched')matched++;if(s==='exception')exceptions++;return '<article class="ibrecord '+s+'"><div><span>'+r.system+'</span><b>'+r.id+'</b><small>'+r.detail+'</small></div><em>'+({'raw':'uncontrolled','pending':'waiting','matched':'linked','exception':'exception queue'})[s]+'</em></article>';}).join('');
      b.querySelector('[data-match]').textContent=records.length?Math.round(matched/records.length*100)+'%':'0%';b.querySelector('[data-ex]').textContent=exceptions;b.querySelector('[data-guess]').textContent='0';b.querySelector('[data-count]').textContent=stage+' / 3';b.querySelector('[data-step]').disabled=stage>=3;
      var notes=[c.rawNote||'The same real-world thing has several local identifiers. Similar text is evidence to examine, not permission to merge.',c.exactNote||'Exact governed identifiers can link automatically when source, format, and scope rules are satisfied.',c.mappedNote||'Approved crosswalks link legitimate local identifiers to the governed identity and preserve the source values.',c.exceptionNote||'Conflicts and nicknames go to a named steward with supporting evidence. No uncertain pair is silently forced into a match.'];b.querySelector('[data-narr]').innerHTML='<b>'+['Observe','Exact-match control','Approved mapping control','Exception control'][stage]+'.</b> '+notes[stage];
    }
    b.querySelector('[data-step]').addEventListener('click',function(){if(stage<3)stage++;paint();});b.querySelector('[data-reset]').addEventListener('click',function(){stage=0;paint();});paint();
  };

  /* ---- boot ---- */
  function boot(){
    injectDroobi();
    document.querySelectorAll('[data-ac]').forEach(function(el){
      var t=el.getAttribute('data-ac');
      if(R[t])try{R[t](el);}catch(e){console.error('academy: render failed for',t,e);}
      else console.warn('academy: unknown component',t);
    });
    initTooltips();
    initChrome();
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot);else boot();
})();
