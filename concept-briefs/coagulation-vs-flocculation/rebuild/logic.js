(function(){
  "use strict";

  /* ---------------- learning record ----------------
     One channel so the OWOS platform can attach a recorder without this page
     changing. Events carry the brief, its version, and the contract, and never
     facility information. With no recorder attached they go nowhere. */
  var OWOS = window.OWOS = window.OWOS || {};
  OWOS.brief = {
    id: "owos:concept-brief:001",
    version: "rebuild.1.0",
    contract: "owos-concept-brief/2",
    namespace: "owos.concept_brief.001"
  };
  OWOS.events = OWOS.events || [];
  OWOS.track = function(name, detail){
    var evt = { event: OWOS.brief.namespace + "." + name, brief: OWOS.brief.id,
      brief_version: OWOS.brief.version, at: new Date().toISOString(), detail: detail || {} };
    OWOS.events.push(evt);
    try { window.dispatchEvent(new CustomEvent("owos:event", {detail: evt})); } catch(e){}
    if (typeof OWOS.recorder === "function") { try { OWOS.recorder(evt); } catch(e){} }
  };

  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------------- definitions with graphics ---------------- */
  var G = { deep:"#141311", ground:"#3a3329", w:"#7dc6e8", wd:"#2b7399",
            am:"#e0a64a", rd:"#e07a63", gn:"#7fb069", mu:"#a29c91", wh:"#f2f1ec" };

  function fig(vb, ids, title, desc, body, cap){
    return '<figure class="def-fig"><svg viewBox="'+vb+'" role="img" aria-labelledby="'+ids[0]+' '+ids[1]+'">'+
      '<title id="'+ids[0]+'">'+title+'</title><desc id="'+ids[1]+'">'+desc+'</desc>'+body+
      '</svg><figcaption>'+cap+'</figcaption></figure>';
  }
  function t(x,y,fill,s,size){ return '<text x="'+x+'" y="'+y+'" font-family="monospace" font-size="'+(size||10)+'" fill="'+fill+'">'+s+'</text>'; }

  var DEFS = [
    { term:"Coagulation",
      meaning:'In federal regulation, "a process using coagulant chemicals and mixing by which colloidal and suspended materials are destabilized and agglomerated into flocs" (40 CFR 141.2).',
      pic:"the chemical entering just before a fast impeller, and the water going cloudy in a different way than it was cloudy before.",
      not:"that the floc is big enough to remove. Destabilised and agglomerated is the start of the job, not the end of it.",
      vb:"0 0 400 150", ids:["cgt","cgd"],
      title:"Particles repelling, then destabilised, then starting to join",
      desc:"Three panels. In the first, separated particles carry like charges and repel. In the second, coagulant has been added and the repulsion is gone. In the third, particles have begun to join into small flocs.",
      body:'<rect width="400" height="150" fill="'+G.deep+'"/>'+
        t(14,24,G.mu,"1. REPELLING")+t(146,24,G.mu,"2. DESTABILISED")+t(288,24,G.mu,"3. STARTING")+
        // panel 1: particles apart with repulsion arcs
        '<g>'+[38,74,110].map(function(x,i){return '<circle cx="'+x+'" cy="'+(60+ (i%2)*32)+'" r="9" fill="'+G.wd+'"/>';}).join('')+
        '<path d="M50 66 L62 66" stroke="'+G.rd+'" stroke-width="2"/><path d="M86 92 L98 92" stroke="'+G.rd+'" stroke-width="2"/>'+
        t(26,124,G.rd,"THEY PUSH APART")+'</g>'+
        // panel 2: coagulant added, no repulsion
        '<g>'+[170,200,230].map(function(x,i){return '<circle cx="'+x+'" cy="'+(60+(i%2)*32)+'" r="9" fill="'+G.wd+'"/>';}).join('')+
        '<path d="M186 34 L196 48" stroke="'+G.am+'" stroke-width="3" marker-end="url(#cA)"/>'+
        t(150,124,G.gn,"REPULSION GONE")+'</g>'+
        // panel 3: joined
        '<g><circle cx="316" cy="66" r="9" fill="'+G.wd+'"/><circle cx="332" cy="74" r="9" fill="'+G.wd+'"/>'+
        '<circle cx="326" cy="88" r="9" fill="'+G.wd+'"/><circle cx="356" cy="62" r="9" fill="'+G.wd+'"/>'+
        '<circle cx="370" cy="74" r="9" fill="'+G.wd+'"/>'+t(286,124,G.w,"SMALL FLOCS FORM")+'</g>'+
        '<defs><marker id="cA" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="'+G.am+'"/></marker></defs>',
      cap:"Willing to join is not joined. That is coagulation's whole output." },

    { term:"Flocculation",
      meaning:'In federal regulation, "a process to enhance agglomeration or collection of smaller floc particles into larger, more easily settleable particles through gentle stirring by hydraulic or mechanical means" (40 CFR 141.2).',
      pic:"large slow paddles in a long basin, water moving but not churning.",
      not:"that it can compensate for a chemical failure. It enhances what exists; it cannot create floc from particles that were never destabilised.",
      vb:"0 0 400 150", ids:["flt","fld"],
      title:"Small flocs growing into large settleable flocs under gentle stirring",
      desc:"Left, many small flocs. A gentle stirring stage in the middle. Right, fewer and much larger flocs which are heavy enough to settle.",
      body:'<rect width="400" height="150" fill="'+G.deep+'"/>'+
        t(14,24,G.mu,"SMALL FLOC IN")+t(300,24,G.mu,"SETTLEABLE OUT")+
        '<g>'+[[30,60],[48,80],[26,96],[52,110],[38,44],[64,62]].map(function(p){return '<circle cx="'+p[0]+'" cy="'+p[1]+'" r="6" fill="'+G.wd+'"/>';}).join('')+'</g>'+
        '<path d="M84 76 L148 76" stroke="'+G.w+'" stroke-width="3" marker-end="url(#fA)"/>'+
        '<g><circle cx="196" cy="76" r="34" fill="none" stroke="'+G.mu+'" stroke-width="1.5" stroke-dasharray="5 4"/>'+
        '<path d="M172 90 Q196 60 220 90" stroke="'+G.w+'" stroke-width="2.5" fill="none"/>'+
        '<path d="M172 66 Q196 96 220 66" stroke="'+G.w+'" stroke-width="2.5" fill="none"/>'+
        t(158,130,G.w,"GENTLE STIRRING")+'</g>'+
        '<path d="M244 76 L292 76" stroke="'+G.w+'" stroke-width="3" marker-end="url(#fA)"/>'+
        '<circle cx="330" cy="66" r="17" fill="'+G.wd+'"/><circle cx="366" cy="92" r="14" fill="'+G.wd+'"/>'+
        '<path d="M330 92 L330 116" stroke="'+G.gn+'" stroke-width="2.5" marker-end="url(#fB)"/>'+
        t(302,140,G.gn,"HEAVY ENOUGH TO FALL")+
        '<defs><marker id="fA" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="'+G.w+'"/></marker>'+
        '<marker id="fB" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="'+G.gn+'"/></marker></defs>',
      cap:"It grows what already exists. It cannot start from nothing." },

    { term:"Rapid mix and gentle stirring",
      meaning:"Two opposite mixing regimes, back to back. Rapid mix disperses the coagulant through all the water while it is still reacting. Flocculation then stirs gently enough for floc to survive.",
      pic:"a small chamber with a fast impeller, then a long basin with slow paddles.",
      not:"a target. EPA directs that mixing intensity must keep falling from the last flocculation stage onward so formed floc is not broken, but the values belong to your design documents.",
      vb:"0 0 400 150", ids:["mxt","mxd"],
      title:"Mixing intensity stepping down through the treatment train",
      desc:"A stepped profile. Intensity is very high in the rapid mix stage, then drops sharply and continues stepping down through flocculation stages and onward toward sedimentation.",
      body:'<rect width="400" height="150" fill="'+G.deep+'"/>'+
        '<line x1="42" y1="30" x2="42" y2="112" stroke="'+G.mu+'" stroke-width="1.5"/>'+
        '<line x1="42" y1="112" x2="386" y2="112" stroke="'+G.mu+'" stroke-width="1.5"/>'+
        t(8,74,G.mu,"MIXING",9)+t(8,86,G.mu,"ENERGY",9)+
        '<path d="M52 40 L104 40 L104 74 L172 74 L172 86 L240 86 L240 96 L308 96 L308 104 L380 104" stroke="'+G.w+'" stroke-width="3.5" fill="none"/>'+
        '<rect x="52" y="40" width="52" height="72" fill="'+G.w+'" opacity=".14"/>'+
        t(54,34,G.am,"RAPID MIX")+t(176,68,G.w,"FLOCCULATION, TAPERING")+
        t(300,124,G.gn,"TOWARD SEDIMENTATION")+
        '<path d="M104 128 L376 128" stroke="'+G.gn+'" stroke-width="2" stroke-dasharray="5 4" marker-end="url(#mA)"/>'+
        '<defs><marker id="mA" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="'+G.gn+'"/></marker></defs>',
      cap:"Down, and it must keep going down. Anything that raises it again breaks floc." },

    { term:"Pin floc",
      meaning:"Small floc that has formed but is not growing into anything settleable.",
      pic:"fine specks suspended throughout, like dust in a sunbeam, not settling.",
      not:"which process failed, or in which direction. EPA documents a plant where pin floc was caused by dosing coagulant at excessive rates, the opposite of the reflex it usually triggers.",
      vb:"0 0 400 150", ids:["pnt","pnd"],
      title:"Pin floc suspended and not settling",
      desc:"Many very small particles distributed evenly through the water column, none of them falling, contrasted with a single large floc that is settling.",
      body:'<rect width="400" height="150" fill="'+G.deep+'"/>'+
        '<rect x="20" y="30" width="170" height="102" fill="'+G.wd+'" opacity=".22"/>'+
        '<g fill="'+G.wh+'" opacity=".85">'+
        [[40,48],[72,42],[110,52],[148,46],[58,70],[96,66],[132,74],[168,62],[46,96],[84,92],[122,100],[160,90],[64,118],[104,122],[142,114]]
        .map(function(p){return '<circle cx="'+p[0]+'" cy="'+p[1]+'" r="2.6"/>';}).join('')+'</g>'+
        t(22,24,G.rd,"NOT SETTLING")+
        '<rect x="222" y="30" width="158" height="102" fill="'+G.wd+'" opacity=".22"/>'+
        '<circle cx="286" cy="52" r="15" fill="'+G.wd+'"/>'+
        '<path d="M286 72 L286 116" stroke="'+G.gn+'" stroke-width="2.5" marker-end="url(#pA)"/>'+
        '<circle cx="340" cy="104" r="13" fill="'+G.wd+'"/>'+
        t(224,24,G.gn,"SETTLING")+
        '<defs><marker id="pA" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="'+G.gn+'"/></marker></defs>',
      cap:"An appearance, not a cause. Three different situations produce it." },

    { term:"Jar test",
      meaning:"A bench-scale simulation using several small vessels dosed differently, mixed, and allowed to settle.",
      pic:"six beakers on a gang stirrer, side by side, each a slightly different condition.",
      not:"what the plant will do. It is evidence from a model of the plant, not a measurement of the plant, and the things it leaves out are exactly where plants fail.",
      vb:"0 0 400 150", ids:["jrt","jrd"],
      title:"What a jar contains and what a basin contains",
      desc:"On the left, six identical beakers on a stirrer. On the right, a basin showing short circuiting, a dead zone, and a transit path to the next process, none of which exist in the jar.",
      body:'<rect width="400" height="150" fill="'+G.deep+'"/>'+
        t(14,24,G.mu,"THE JAR HAS")+
        '<g>'+[22,54,86,118,150].map(function(x){return '<rect x="'+x+'" y="52" width="22" height="40" rx="2" fill="'+G.wd+'" opacity=".8"/>';}).join('')+'</g>'+
        '<line x1="18" y1="46" x2="178" y2="46" stroke="'+G.mu+'" stroke-width="2"/>'+
        t(22,116,G.gn,"CHEMISTRY, SIDE BY SIDE")+
        '<line x1="196" y1="20" x2="196" y2="140" stroke="#4a4741" stroke-width="1" stroke-dasharray="4 4"/>'+
        t(210,24,G.mu,"THE BASIN ALSO HAS")+
        '<rect x="214" y="46" width="168" height="52" fill="none" stroke="'+G.mu+'" stroke-width="1.5"/>'+
        '<path d="M214 60 Q290 52 382 60" stroke="'+G.rd+'" stroke-width="2.5" fill="none" stroke-dasharray="6 4"/>'+
        t(228,42,G.rd,"SHORT CIRCUIT")+
        '<circle cx="242" cy="86" r="9" fill="'+G.am+'" opacity=".4"/>'+t(256,90,G.am,"DEAD ZONE")+
        '<path d="M382 78 L382 122" stroke="'+G.rd+'" stroke-width="2.5" marker-end="url(#jA)"/>'+
        t(268,136,G.rd,"TRANSIT THAT BREAKS FLOC")+
        '<defs><marker id="jA" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="'+G.rd+'"/></marker></defs>',
      cap:"When the jar and the plant disagree, the difference between them is the finding." }
  ];

  document.getElementById("defs").innerHTML = DEFS.map(function(d){
    return '<div class="def"><div class="def-text"><h3>'+d.term+'</h3>'+
      '<p>'+d.meaning+'</p>'+
      '<p class="pic"><b>Picture it:</b> '+d.pic+'</p>'+
      '<p class="not"><b>What it does not tell you:</b> '+d.not+'</p></div>'+
      fig(d.vb, d.ids, d.title, d.desc, d.body, d.cap)+'</div>';
  }).join("");

  /* ---------------- interactive 1: the dose window ---------------- */
  var X0=90, X1=850, YB=270, YT=60;
  function perf(x){ // x is 0..1 dose; a window that fails on both sides
    var d=(x-0.45)/0.20; return Math.exp(-d*d);
  }
  function px(x){ return X0 + x*(X1-X0); }
  function py(v){ return YB - v*(YB-YT); }
  var curvePts=[]; for(var i=0;i<=140;i++){ var x=i/140; curvePts.push([px(x),py(perf(x))]); }
  var dPath="M"+curvePts.map(function(p){return p[0].toFixed(1)+" "+p[1].toFixed(1);}).join("L");
  document.getElementById("doseCurve").setAttribute("d", dPath);
  document.getElementById("doseFill").setAttribute("d", dPath+"L"+X1+" "+YB+"L"+X0+" "+YB+"Z");

  var DOSE=[
    { x:0.16, label:"Too little",
      title:"Particles are still stable",
      body:["Not enough coagulant to overcome the repulsion between particles, so they stay apart and nothing aggregates.",
            "In the basin this looks like almost no floc at all. Adding more is the correct move here, and this is the one case where the reflex works."] },
    { x:0.45, label:"In the window",
      title:"This is what you are looking for",
      body:["Repulsion is overcome, particles are able to join, and flocculation has something to work with.",
            "The window has width but it is not infinite, and where it sits depends on your water, your coagulant, and your pH."] },
    { x:0.72, label:"Past the window",
      title:"Going backwards, and it looks like going forwards",
      body:["Performance is falling, and it looks exactly like the too-little case from the walkway. Small floc, poor settling.",
            "An operator who assumes more is better reads this as needing more, and every increase walks further from the answer."] },
    { x:0.93, label:"Well past it",
      title:"The documented failure",
      body:["Charge reversed, particles repelling again, plus the pH dragged down by the alkalinity the coagulant consumed. Two problems now, one of them self-inflicted.",
            "This is the state EPA describes: excessive dosing producing pin floc that was difficult to settle and filter. And more sludge to handle for the trouble."] }
  ];
  var doseDot=document.getElementById("doseDot"), doseDrop=document.getElementById("doseDrop"),
      doseOut=document.getElementById("doseReadout");
  function drawDose(i){
    var d=DOSE[i], cx=px(d.x), cy=py(perf(d.x));
    doseDot.setAttribute("cx",cx); doseDot.setAttribute("cy",cy);
    doseDrop.setAttribute("x1",cx); doseDrop.setAttribute("x2",cx); doseDrop.setAttribute("y1",cy);
    var h='<span class="rk">'+d.label+'</span><p><b style="color:var(--white)">'+d.title+'</b></p>';
    d.body.forEach(function(p){ h+="<p>"+p+"</p>"; });
    doseOut.innerHTML=h;
  }
  [].slice.call(document.querySelectorAll(".dose-btn")).forEach(function(b){
    b.addEventListener("click", function(){
      document.querySelectorAll(".dose-btn").forEach(function(x){x.setAttribute("aria-pressed","false");});
      b.setAttribute("aria-pressed","true");
      drawDose(+b.dataset.dose);
      OWOS.track("interaction.dose.state",{state:DOSE[+b.dataset.dose].label});
    });
  });
  drawDose(1);

  /* ---------------- interactive 2: pin floc causes ---------------- */
  var PIN=[
    { label:"Marginal chemistry", verdict:"WOULD HELP",  colour:G.gn,
      title:"Particles are only just destabilised",
      body:["Chemistry is close but not quite there, so floc starts and stalls.",
            "Evidence that distinguishes it: a jar series finds a clearly better dose above the current setpoint.",
            "This is the one case where adding coagulant is the right answer."] },
    { label:"Inadequate contact", verdict:"WOULD NOT HELP", colour:G.am,
      title:"The chemistry worked and is not being delivered",
      body:["Flocculation energy too low, residence time too short, the basin short circuiting, or floc broken in transit.",
            "Evidence that distinguishes it: the jar at the current dose looks good while the plant does not.",
            "Adding coagulant cannot fix a basin. It masks the fault while the fault stays unfound."] },
    { label:"Excessive dose", verdict:"WOULD MAKE IT WORSE", colour:G.rd,
      title:"Already past the window",
      body:["Charge reversed, particles repelling again, and pH dragged down by consumed alkalinity.",
            "Evidence that distinguishes it: a jar series finds better performance <b>below</b> the current setpoint. This is the step most often skipped.",
            "This is the case EPA documented. Adding more is what caused it."] }
  ];
  var pinOut=document.getElementById("pinReadout"), pinVerdict=document.getElementById("pinVerdict");
  function drawPin(i){
    document.querySelectorAll(".pin-path").forEach(function(p){
      var on = +p.dataset.c === i;
      p.setAttribute("stroke", on ? PIN[i].colour : "#4a4741");
      p.setAttribute("stroke-width", on ? "6" : "5");
    });
    document.querySelectorAll(".pin-cause rect").forEach(function(r,n){
      r.setAttribute("stroke", n===i ? PIN[i].colour : "#4a4741");
    });
    pinVerdict.textContent = PIN[i].verdict;
    pinVerdict.setAttribute("fill", PIN[i].colour);
    var h='<span class="rk">'+PIN[i].label+'</span><p><b style="color:var(--white)">'+PIN[i].title+'</b></p>';
    PIN[i].body.forEach(function(p){ h+="<p>"+p+"</p>"; });
    pinOut.innerHTML=h;
  }
  [].slice.call(document.querySelectorAll(".pin-btn")).forEach(function(b){
    b.addEventListener("click", function(){
      document.querySelectorAll(".pin-btn").forEach(function(x){x.setAttribute("aria-pressed","false");});
      b.setAttribute("aria-pressed","true");
      drawPin(+b.dataset.c);
      OWOS.track("interaction.pinfloc.cause",{cause:PIN[+b.dataset.c].label});
    });
  });
  pinOut.innerHTML='<span class="rk">Pick a cause</span><p>All three produce the same appearance. Two of them get worse if you add coagulant.</p>';

  /* ---------------- flip cards ---------------- */
  var FLIPS=[
    ["Federal regulation puts mixing inside one of these two definitions. Which, and why does it matter?",
     "Coagulation. The regulation defines it as using coagulant chemicals <em>and mixing</em> to destabilise and agglomerate into flocs. So coagulation is not purely chemistry, and the clean chemistry-against-physics split is a shorthand, not the regulatory line."],
    ["The floc is poor and you have already increased the dose twice with no improvement. What does that tell you?",
     "That the dose is not the variable, or that you are on the wrong side of the window. Two failed increases is evidence, not an argument for a third."],
    ["Jar tests look good. The plant looks bad. Which is wrong?",
     "Neither. The chemistry is demonstrably available, so the fault is in what the plant has that the jar does not: hydraulics, residence time, and transit."],
    ["Why is running jar doses <em>below</em> your current setpoint the step most often skipped?",
     "Because the operator is looking for more, not for a window. It is also the only test that catches an overdose, which is the case EPA documented."],
    ["What does flocculation do that coagulation does not?",
     "Grows smaller floc into larger, more easily settleable particles through gentle stirring. It enhances what exists. It cannot create floc from particles that were never destabilised."],
    ["A filter run is getting shorter. Where do you look first?",
     "Upstream. EPA states that optimal coagulant dosage is critical to filter performance. A filter often inherits a conditioning problem and reports it late."]
  ];
  document.getElementById("flips").innerHTML = FLIPS.map(function(f){
    return '<button type="button" class="flip" aria-pressed="false"><span class="flip-in">'+
      '<span class="flip-f"><span class="flip-tag">Question</span><p class="q">'+f[0]+'</p>'+
      '<span class="flip-hint">Tap to reveal</span></span>'+
      '<span class="flip-b"><span class="flip-tag">Answer</span><p class="a">'+f[1]+'</p>'+
      '<span class="flip-hint">Tap to go back</span></span></span></button>';
  }).join("");
  [].slice.call(document.querySelectorAll(".flip")).forEach(function(card){
    card.addEventListener("click", function(){
      var open = card.getAttribute("aria-pressed")==="true";
      card.setAttribute("aria-pressed", open?"false":"true");
      if(!open) OWOS.track("check.flipcard.revealed",{card:(card.querySelector(".q")||{}).textContent||""});
    });
  });

  /* ---------------- work product ---------------- */
  var QUESTIONS=[
    { id:"which", q:"Which of the two processes is failing, and what is your evidence?",
      why:"This is the question the appearance cannot answer for you.",
      model:"I do not know yet, and that is the finding rather than an evasion. What I have is poor floc in the flocculation basin, which is consistent with marginal chemistry, inadequate contact, and excessive dose. What I need is one jar series at the current water spanning doses both above and below the present setpoint, compared against what the plant is producing on that same water. If the jar finds better performance at a different dose, it is chemistry and I know the direction. If the jar at the current dose looks good while the plant does not, it is not chemistry at all." },
    { id:"window", q:"Which side of the window are you on, and how would you know?",
      why:"Performance falls on both sides, so direction cannot be assumed.",
      model:"Unknown until I test below the setpoint, which is the step I would normally skip. The plant has increased dose twice without improvement, and that pattern fits being on the high side at least as well as it fits needing more. Supporting evidence would be pH and alkalinity trending down as dose went up, since these coagulants consume alkalinity, and sludge production rising. I would run the jar series before any further increase, because if we are on the high side then every increase so far has moved us further from the answer." },
    { id:"physical", q:"What changed physically, and when did anyone last check?",
      why:"The cheap lever is chemical. The likely cause is often not.",
      model:"Things to establish before touching chemistry: is every flocculator running, and at the speed it should be. Has plant flow increased, which shortens residence time. Is there any sign of short circuiting, meaning water leaving the basin in much less time than the volumetric residence time. Have the inlet and outlet conditions between flocculation and sedimentation been checked for anything that would break formed floc, since EPA directs that velocity gradient must keep falling from the last flocculation stage onward. None of these requires a chemical change to investigate." },
    { id:"cost", q:"If you increase the dose and it works, what else did you just decide?",
      why:"The invoice is not the whole cost, and it arrives in someone else's budget.",
      model:"More residuals to thicken, dewater, haul, and dispose of, arriving months later in a different budget line reported by a different person, with no trace back to this shift. Alkalinity consumed, so a pH consequence to watch and possibly to correct with another chemical. And if the real cause was physical, a masked fault that stays unfound while the plant keeps paying to work around it. None of that argues against increasing the dose when the dose is the problem. It argues for establishing that it is the problem first." }
  ];
  var KEY="owos-cb001-rebuild-work", ws=document.getElementById("workspace"),
      status=document.getElementById("wpStatus"), timers={};
  QUESTIONS.forEach(function(item,i){
    var box=document.createElement("div"); box.className="wq";
    box.innerHTML='<h3>'+(i+1)+'. '+item.q+'</h3><p class="why">'+item.why+'</p>'+
      '<textarea id="ta-'+item.id+'" aria-label="'+item.q.replace(/"/g,"&quot;")+'" '+
      'placeholder="Watch it answered, or write your own. Neither is required."></textarea>'+
      '<div class="wq-controls"><button type="button" data-watch="'+item.id+'">Watch it answered</button>'+
      '<button type="button" data-stop="'+item.id+'">Stop</button>'+
      '<button type="button" data-clear="'+item.id+'">Clear</button>'+
      '<span class="status" data-status="'+item.id+'"></span></div>';
    ws.appendChild(box);
  });
  function setStatus(id,text,cls){ var el=document.querySelector('[data-status="'+id+'"]');
    if(el){ el.textContent=text||""; el.className="status"+(cls?" "+cls:""); } }
  function stopTyping(id){ if(timers[id]){clearInterval(timers[id]); delete timers[id];}
    var ta=document.getElementById("ta-"+id); if(ta) ta.classList.remove("typing"); }
  function typeInto(id,text,done){
    var ta=document.getElementById("ta-"+id); stopTyping(id);
    ta.value=""; ta.classList.add("typing"); setStatus(id,"writing...","live");
    if(reduced){ ta.value=text; ta.classList.remove("typing"); setStatus(id,"model answer shown","done"); if(done)done(); return; }
    var i=0;
    timers[id]=setInterval(function(){
      var burst=2+Math.floor(Math.random()*3);
      ta.value=text.slice(0,i+=burst); ta.scrollTop=ta.scrollHeight;
      if(i>=text.length){ stopTyping(id); ta.value=text; setStatus(id,"model answer shown","done"); if(done)done(); }
    },16);
  }
  ws.addEventListener("click",function(e){
    var b=e.target.closest("button"); if(!b) return;
    if(b.dataset.watch){ var q=QUESTIONS.filter(function(x){return x.id===b.dataset.watch;})[0];
      OWOS.track("work.answer.watched",{question:q.id}); typeInto(q.id,q.model); }
    if(b.dataset.stop){ stopTyping(b.dataset.stop); setStatus(b.dataset.stop,"stopped, edit freely",""); }
    if(b.dataset.clear){ stopTyping(b.dataset.clear); document.getElementById("ta-"+b.dataset.clear).value=""; setStatus(b.dataset.clear,"cleared",""); }
  });
  ws.addEventListener("input",function(e){
    if(e.target.tagName==="TEXTAREA"){ var id=e.target.id.replace("ta-","");
      stopTyping(id); setStatus(id,"your words",""); OWOS.track("work.answer.authored",{question:id}); }
  });
  document.getElementById("watchAll").addEventListener("click",function(){
    var n=0;
    (function next(){
      if(n>=QUESTIONS.length){ status.textContent="All four answered. Edit any of them, or download."; return; }
      var q=QUESTIONS[n++];
      document.getElementById("ta-"+q.id).scrollIntoView({block:"center",behavior:reduced?"auto":"smooth"});
      typeInto(q.id,q.model,function(){ setTimeout(next,320); });
    })();
  });
  document.getElementById("saveAll").addEventListener("click",function(){
    var out={}; QUESTIONS.forEach(function(q){ out[q.id]=document.getElementById("ta-"+q.id).value; });
    try{ localStorage.setItem(KEY,JSON.stringify(out)); status.textContent="Saved to this browser. It will be here when you come back."; }
    catch(e){ status.textContent="This browser refused local storage, so nothing was saved. Use Download instead."; }
  });
  document.getElementById("exportAll").addEventListener("click",function(){
    var lines=["# Poor floc: four questions before a setpoint changes","",
      "_Worked from the OWOS Concept Brief: Coagulation and Flocculation._",
      "_Conceptual reasoning only. Plant decisions require approved procedures and qualified judgment._",""];
    QUESTIONS.forEach(function(q,i){ lines.push("## "+(i+1)+". "+q.q,"",(document.getElementById("ta-"+q.id).value||"_Not answered._"),""); });
    var blob=new Blob([lines.join("\n")],{type:"text/markdown"}), a=document.createElement("a");
    a.href=URL.createObjectURL(blob); a.download="coagulation-four-questions.md";
    document.body.appendChild(a); a.click(); document.body.removeChild(a);
    setTimeout(function(){ URL.revokeObjectURL(a.href); },1500);
    OWOS.track("work.exported",{format:"markdown"}); status.textContent="Downloaded as Markdown.";
  });
  document.getElementById("clearAll").addEventListener("click",function(){
    QUESTIONS.forEach(function(q){ stopTyping(q.id); document.getElementById("ta-"+q.id).value=""; setStatus(q.id,"",""); });
    try{ localStorage.removeItem(KEY); }catch(e){}
    status.textContent="Cleared, including anything saved in this browser.";
  });
  try{ var saved=JSON.parse(localStorage.getItem(KEY)||"{}"), restored=false;
    QUESTIONS.forEach(function(q){ if(saved[q.id]){ document.getElementById("ta-"+q.id).value=saved[q.id]; restored=true; } });
    if(restored) status.textContent="Restored what you had in this browser.";
  }catch(e){}

  /* ---------------- reading progress ---------------- */
  (function(){
    var fill=document.getElementById("railFill"), stage=document.getElementById("railStage"),
        left=document.getElementById("railLeft");
    if(!fill) return;
    var TOTAL=15, marks=[].slice.call(document.querySelectorAll("section[aria-labelledby]"));
    var names=["START HERE","IN 30 SECONDS","THE PROBLEM","THE WORDS","THE WINDOW","PIN FLOC",
               "BACK TO THE SHIFT","CHECK YOURSELF","PUT IT TO WORK","WHERE COST LANDS",
               "SOURCES","KEEP LEARNING","BEFORE YOU LEAVE","PRACTICE"];
    function update(){
      var max=document.documentElement.scrollHeight-window.innerHeight;
      var pct=max>0?Math.min(1,Math.max(0,window.scrollY/max)):0;
      fill.style.width=(pct*100).toFixed(1)+"%";
      left.textContent=Math.max(0,Math.round(TOTAL*(1-pct)));
      var cur=0; for(var i=0;i<marks.length;i++){ if(marks[i].getBoundingClientRect().top<=120) cur=i; }
      stage.textContent=names[cur]||names[names.length-1];
    }
    var ticking=false;
    window.addEventListener("scroll",function(){ if(ticking)return; ticking=true;
      requestAnimationFrame(function(){ update(); ticking=false; }); },{passive:true});
    window.addEventListener("resize",update); update();
  })();

  /* ---------------- completion events ---------------- */
  OWOS.track("started",{});
  (function(){
    var fired={};
    var io="IntersectionObserver" in window ? new IntersectionObserver(function(es){
      es.forEach(function(e){
        if(!e.isIntersecting) return;
        var id=e.target.getAttribute("aria-labelledby")||e.target.id;
        if(fired[id]) return; fired[id]=true;
        OWOS.track("section.reached",{section:id});
        if(id==="rc-t") OWOS.track("completed",{});
      });
    },{threshold:.4}) : null;
    if(io) document.querySelectorAll("section[aria-labelledby]").forEach(function(x){io.observe(x);});
  })();

  /* ---------------- top drawers ---------------- */
  (function(){
    var backdrop=document.getElementById("backdrop");
    var drawers={graph:document.getElementById("graphDrawer"), community:document.getElementById("commDrawer")};
    var openName=null, lastTrigger=null;
    function close(){
      if(!openName) return;
      var d=drawers[openName];
      d.classList.remove("on"); backdrop.classList.remove("on");
      window.setTimeout(function(){ d.hidden=true; backdrop.hidden=true; },200);
      document.querySelectorAll("[data-open]").forEach(function(b){ b.setAttribute("aria-expanded","false"); });
      document.body.style.overflow="";
      if(lastTrigger) lastTrigger.focus();
      if(location.hash==="#"+openName) history.back();
      OWOS.track("drawer.closed",{drawer:openName}); openName=null;
    }
    function open(name,trigger){
      if(openName) close();
      var d=drawers[name]; if(!d) return;
      lastTrigger=trigger||null; backdrop.hidden=false; d.hidden=false;
      window.requestAnimationFrame(function(){ backdrop.classList.add("on"); d.classList.add("on"); });
      if(trigger) trigger.setAttribute("aria-expanded","true");
      document.body.style.overflow="hidden";
      d.querySelector(".drawer-close").focus(); openName=name;
      history.pushState({drawer:name},"","#"+name);
      OWOS.track("drawer.opened",{drawer:name});
    }
    document.querySelectorAll("[data-open]").forEach(function(b){
      b.addEventListener("click",function(){ open(b.dataset.open,b); }); });
    document.addEventListener("click",function(e){ if(e.target.closest("[data-close]")) close(); });
    backdrop.addEventListener("click",close);
    document.addEventListener("keydown",function(e){
      if(e.key==="Escape"&&openName) close();
      if(e.key==="Tab"&&openName){
        var d=drawers[openName];
        var f=d.querySelectorAll("button, a[href], [tabindex]:not([tabindex='-1'])");
        if(!f.length) return;
        var first=f[0], last=f[f.length-1];
        if(e.shiftKey&&document.activeElement===first){ e.preventDefault(); last.focus(); }
        else if(!e.shiftKey&&document.activeElement===last){ e.preventDefault(); first.focus(); }
      }
    });
    window.addEventListener("popstate",function(){ if(openName) close(); });
  })();
})();
