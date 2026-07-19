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
    var b=shell(el,'<div class="trirow"><div class="trisvg"><svg viewBox="0 0 260 200">'+
      '<polygon points="130,24 236,180 24,180" fill="#EAF5FC" stroke="#0A78BA" stroke-width="2"/>'+
      '<text x="130" y="16" text-anchor="middle" font-size="12" fill="#0F1728" font-weight="700">'+L[0]+'</text>'+
      '<text x="240" y="196" text-anchor="end" font-size="12" fill="#0F1728" font-weight="700">'+L[1]+'</text>'+
      '<text x="20" y="196" text-anchor="start" font-size="12" fill="#0F1728" font-weight="700">'+L[2]+'</text>'+
      '<text x="130" y="130" text-anchor="middle" font-size="11" fill="#0A78BA" font-weight="700">Quality</text>'+
      '<text x="130" y="146" text-anchor="middle" font-size="9" fill="#44546A">sits inside</text></svg></div>'+
      '<div class="tricontrols">'+[0,1,2].map(function(i){return '<div class="ctl"><div class="nm">'+L[i]+
        '<small>'+['how much work','how long','how much money'][i]+'</small></div><div class="step" data-k="'+i+'">'+
        '<button data-d="-1">&#8722;</button><span class="v">3</span><button data-d="1">+</button></div></div>';}).join('')+
      '<div class="qbadge" data-badge></div></div></div>');
    var val=[3,3,3];var badge=b.querySelector('[data-badge]');
    function upd(){
      var slack=(val[1]-3)+(val[2]-3)-(val[0]-3);
      var t,col,bg;
      if(slack>=1){t='Comfortable. Time and money cover the scope.';col='#0E8A64';bg='#E7F6F0';}
      else if(slack===0){t='Balanced. Every corner is pulling its weight.';col='#0A78BA';bg='#EAF5FC';}
      else{t='Quality at risk. Scope is running ahead of time and money.';col='#D64545';bg='#FCEDED';}
      badge.textContent=t;badge.style.color=col;badge.style.background=bg;
    }
    b.querySelectorAll('.step').forEach(function(st){var k=+st.dataset.k,v=st.querySelector('.v');
      st.querySelectorAll('button').forEach(function(btn){btn.addEventListener('click',function(){
        val[k]=Math.max(1,Math.min(5,val[k]+ +btn.dataset.d));v.textContent=val[k];upd();
      });});
    });upd();
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
