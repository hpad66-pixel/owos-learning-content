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
