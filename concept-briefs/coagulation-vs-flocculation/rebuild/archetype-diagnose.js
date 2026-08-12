/* Diagnose archetype.
   The learner does not select a pre-authored state. They face a case whose cause
   is hidden, spend a limited budget gathering evidence, commit to a diagnosis
   before they are told, choose an action, and live with the consequence. Adding
   coagulant to an overdose makes the water worse and costs them the shift.

   Predict, commit, reveal, reconcile. The learning is in the gap between what
   they committed to and what was true. */
(function(){
  "use strict";
  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var track = (window.OWOS && window.OWOS.track) || function(){};

  var CAUSES = {
    chem: { key:"chem", name:"Marginal chemistry",
      truth:"The chemistry was close but not there. Particles were only just destabilised, so floc started and stalled." },
    contact:{ key:"contact", name:"Inadequate contact",
      truth:"The chemistry was fine and was not being delivered. A flocculator was running slow, so floc never had the contact to grow." },
    over: { key:"over", name:"Excessive dose",
      truth:"Already past the window. Charge reversed, particles repelling again, and the pH dragged down by consumed alkalinity." }
  };

  // Evidence: what each test returns depends on the hidden cause. Some tests are
  // decisive, some are cheap and tell you nothing, which is the point.
  var EVIDENCE = [
    { id:"look", label:"Look at the basin again", cost:0,
      result:{ chem:"Small floc, not settling. Same as before.",
               contact:"Small floc, not settling. Same as before.",
               over:"Small floc, not settling. Same as before." },
      decisive:false,
      note:"Free, and it cannot separate anything. All three look identical from the walkway. That is the whole problem." },
    { id:"above", label:"Jar test above the current dose", cost:1,
      result:{ chem:"Noticeably better floc at a higher dose.",
               contact:"No better. Same poor floc across the range.",
               over:"Worse. Floc degrades further as dose rises." },
      decisive:true,
      note:"Useful, and on its own it can mislead. A poor result here does not tell you which of the other two you have." },
    { id:"below", label:"Jar test below the current dose", cost:1,
      result:{ chem:"Worse. Floc degrades as dose falls.",
               contact:"No better. Same poor floc across the range.",
               over:"Noticeably better floc at a lower dose." },
      decisive:true,
      note:"The step most often skipped, and the only one that catches an overdose. Nobody looks down when they are looking for more." },
    { id:"mech", label:"Check flocculator speed and plant flow", cost:1,
      result:{ chem:"Flocculators at set speed. Flow normal.",
               contact:"One flocculator running well below set speed.",
               over:"Flocculators at set speed. Flow normal." },
      decisive:true,
      note:"Cheap, physical, and almost never done first because it is not the operator's lever." },
    { id:"ph", label:"Pull the pH and alkalinity trend", cost:1,
      result:{ chem:"pH and alkalinity steady.",
               contact:"pH and alkalinity steady.",
               over:"pH drifting down. Alkalinity falling as dose rose." },
      decisive:true,
      note:"Corroborates an overdose. These coagulants consume alkalinity, so a rising dose leaves a trace." }
  ];

  var ACTIONS = [
    { id:"up",   label:"Increase the coagulant dose" },
    { id:"down", label:"Decrease the coagulant dose" },
    { id:"mech", label:"Investigate the basin mechanically" },
    { id:"hold", label:"Change nothing yet, gather more" }
  ];

  // Outcome depends on the true cause, not on what the learner believed.
  var OUTCOME = {
    chem:   { up:  ["better","Floc improves within a basin turnover. Settled water clears."],
              down:["worse","Floc collapses further. You were already short and went shorter."],
              mech:["same","Nothing mechanical to find. A shift spent, the water unchanged."],
              hold:["same","No change, and the water is still poor. Holding is safe and it is not free."] },
    contact:{ up:  ["same","No improvement, and the chemical spend is up. The fault is still there, now partly masked."],
              down:["worse","Now you have a contact problem and a chemistry problem."],
              mech:["better","The slow flocculator is found and corrected. Floc grows within a turnover."],
              hold:["same","No change. The fault is mechanical and it will not resolve itself."] },
    over:   { up:  ["worse","Worse again. You are on the far side of the window walking away from it, and making sludge doing it."],
              down:["better","Floc improves as the dose comes down. The window was behind you."],
              mech:["same","Nothing mechanical to find. A shift spent, the water unchanged."],
              hold:["same","No change, and every hour at this dose is producing residuals you will pay to handle."] }
  };

  var CASES = ["chem","contact","over"];

  var state = { idx:0, cause:null, spent:0, gathered:{}, committed:null, acted:null, phase:"gather" };
  var root = document.getElementById("dx");
  if(!root) return;

  function startCase(i){
    state = { idx:i, cause:CASES[i], spent:0, gathered:{}, committed:null, acted:null, phase:"gather" };
    render();
    track("archetype.diagnose.case_started", {case:i+1});
  }

  function waterSvg(mode){
    var specks = mode==="better"
      ? '<circle cx="70" cy="52" r="13" fill="#2b7399"/><circle cx="128" cy="46" r="11" fill="#2b7399"/>'+
        '<circle cx="96" cy="86" r="15" fill="#2b7399"/>'+
        '<path d="M96 104 L96 126" stroke="#7fb069" stroke-width="2.5" marker-end="url(#dxA)"/>'
      : mode==="worse"
      ? '<g fill="#f2f1ec" opacity=".9">'+[[36,40],[62,34],[92,44],[122,36],[152,46],[46,64],[76,58],[106,68],[136,60],[166,70],[40,90],[70,84],[100,94],[130,86],[160,96],[54,116],[88,110],[120,118],[150,112]].map(function(p){return '<circle cx="'+p[0]+'" cy="'+p[1]+'" r="2.4"/>';}).join('')+'</g>'
      : '<g fill="#f2f1ec" opacity=".78">'+[[40,48],[74,42],[110,52],[146,46],[58,72],[96,66],[132,76],[46,98],[84,92],[122,102],[158,90]].map(function(p){return '<circle cx="'+p[0]+'" cy="'+p[1]+'" r="2.6"/>';}).join('')+'</g>';
    var label = mode==="better" ? ["SETTLING","#7fb069"] : mode==="worse" ? ["WORSE THAN YOU STARTED","#e07a63"] : ["UNCHANGED","#a29c91"];
    return '<svg viewBox="0 0 200 150" role="img" aria-label="Water condition: '+label[0].toLowerCase()+'" style="width:200px;height:150px;flex:0 0 auto">'+
      '<rect width="200" height="150" fill="#141311"/><rect x="14" y="20" width="172" height="112" fill="#2b7399" opacity=".2"/>'+
      specks+'<text x="14" y="146" font-family="monospace" font-size="10" fill="'+label[1]+'">'+label[0]+'</text>'+
      '<defs><marker id="dxA" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#7fb069"/></marker></defs></svg>';
  }

  function render(){
    var h = '<div class="dx-head"><span class="dx-case">CASE '+(state.idx+1)+' OF 3</span>'+
      '<span class="dx-cost">SHIFTS SPENT <b>'+state.spent+'</b></span></div>'+
      '<p class="dx-symptom">Poor floc in the flocculation basin. It will not grow and it will not '+
      'settle. Three things could be causing it. You do not know which.</p>';

    // ---- evidence
    h += '<div class="dx-block"><h4>1. Gather what you need. Every test costs a shift except looking.</h4><div class="dx-ev">';
    EVIDENCE.forEach(function(e){
      var got = state.gathered[e.id];
      h += '<button type="button" class="dx-btn'+(got?" got":"")+'" data-ev="'+e.id+'"'+
           (got||state.phase!=="gather"?' disabled':'')+'>'+e.label+
           '<span class="dx-tag">'+(e.cost?"1 shift":"free")+'</span></button>';
    });
    h += '</div>';
    var results = EVIDENCE.filter(function(e){ return state.gathered[e.id]; });
    if(results.length){
      h += '<div class="dx-results">';
      results.forEach(function(e){
        h += '<p><b>'+e.label+':</b> '+e.result[state.cause]+'</p>';
      });
      h += '</div>';
    }
    h += '</div>';

    // ---- commit
    h += '<div class="dx-block"><h4>2. Commit. You are not told first.</h4><div class="dx-ev">';
    Object.keys(CAUSES).forEach(function(k){
      h += '<button type="button" class="dx-btn'+(state.committed===k?" chosen":"")+'" data-dx="'+k+'"'+
           (state.phase!=="gather"?' disabled':'')+'>'+CAUSES[k].name+'</button>';
    });
    h += '</div></div>';

    // ---- action
    if(state.committed){
      h += '<div class="dx-block"><h4>3. Act on it.</h4><div class="dx-ev">';
      ACTIONS.forEach(function(a){
        h += '<button type="button" class="dx-btn'+(state.acted===a.id?" chosen":"")+'" data-act="'+a.id+'"'+
             (state.phase!=="gather"?' disabled':'')+'>'+a.label+'</button>';
      });
      h += '</div></div>';
    }

    // ---- outcome and reconcile
    if(state.phase==="done"){
      var o = OUTCOME[state.cause][state.acted];
      var right = state.committed===state.cause;
      h += '<div class="dx-out '+o[0]+'">'+
           '<div class="dx-out-txt">'+
           '<span class="dx-verdict '+(right?"ok":"no")+'">'+(right?"You had it right":"You had it wrong")+'</span>'+
           '<p><b>What actually happened.</b> '+o[1]+'</p>'+
           '<p><b>The cause was '+CAUSES[state.cause].name.toLowerCase()+'.</b> '+CAUSES[state.cause].truth+'</p>'+
           '</div>'+waterSvg(o[0])+'</div>';

      h += '<div class="dx-block"><h4>4. Reconcile. What the evidence was worth.</h4><div class="dx-recon">';
      EVIDENCE.forEach(function(e){
        var used = !!state.gathered[e.id];
        var wouldTell = e.decisive;
        var cls = used ? (wouldTell?"good":"waste") : (wouldTell?"missed":"skip");
        var verdict = used ? (wouldTell?"You bought it, and it told you something":"You bought it, and it could not tell you anything")
                           : (wouldTell?"You skipped it, and it would have helped":"You skipped it, and it would not have helped");
        h += '<p class="'+cls+'"><b>'+e.label+'.</b> '+verdict+'. '+e.note+'</p>';
      });
      h += '</div></div>';
      h += '<div class="dx-next"><button type="button" class="dx-btn primary" data-next="1">'+
           (state.idx<2?"Next case":"Start again from case 1")+'</button>'+
           '<button type="button" class="dx-btn" data-retry="1">Retry this case</button></div>';
    }

    root.innerHTML = h;
  }

  root.addEventListener("click", function(ev){
    var b = ev.target.closest("button"); if(!b || b.disabled) return;
    if(b.dataset.ev){
      var e = EVIDENCE.filter(function(x){return x.id===b.dataset.ev;})[0];
      state.gathered[e.id]=true; state.spent += e.cost;
      track("archetype.diagnose.evidence",{evidence:e.id,cost:e.cost});
      render(); return;
    }
    if(b.dataset.dx){ state.committed=b.dataset.dx;
      track("archetype.diagnose.committed",{to:b.dataset.dx,spent:state.spent,evidence:Object.keys(state.gathered).length});
      render(); return; }
    if(b.dataset.act){
      state.acted=b.dataset.act; state.phase="done"; state.spent += 1;
      var right = state.committed===state.cause;
      track("archetype.diagnose.resolved",{cause:state.cause,committed:state.committed,action:state.acted,
        correct:right,outcome:OUTCOME[state.cause][state.acted][0],shifts:state.spent});
      render();
      root.querySelector(".dx-out").scrollIntoView({block:"center",behavior:reduced?"auto":"smooth"});
      return;
    }
    if(b.dataset.next){ startCase((state.idx+1)%3); root.scrollIntoView({block:"start",behavior:reduced?"auto":"smooth"}); return; }
    if(b.dataset.retry){ startCase(state.idx); root.scrollIntoView({block:"start",behavior:reduced?"auto":"smooth"}); return; }
  });

  startCase(0);
})();
