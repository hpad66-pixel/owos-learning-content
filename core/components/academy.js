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
    if(lens){lens.querySelectorAll('button').forEach(function(b){
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
    (c.options||[]).map(function(o,i){return '<button class="opt" data-i="'+i+'" data-c="'+(o[1]?1:0)+'">'+o[0]+'</button>';}).join('')+
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
    (c.options||[]).map(function(o,i){return '<button class="opt" data-i="'+i+'" data-c="'+(o[1]?1:0)+'">'+o[0]+'</button>';}).join('')+
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
