(function(){
  "use strict";
  var body=document.body;
  var moduleId=body.dataset.module||"course";
  var storageKey="mbm001:"+moduleId;
  var saved={requirements:{},lens:"foundation",artifact:{}};
  try{saved=Object.assign(saved,JSON.parse(localStorage.getItem(storageKey)||"{}"));}catch(error){}
  function persist(){localStorage.setItem(storageKey,JSON.stringify(saved));}
  function announce(message,tone){
    var live=document.getElementById("live");
    if(!live)return;
    live.textContent=message;
    live.className="feedback show "+(tone||"");
  }
  function mark(id){
    if(!id)return;
    saved.requirements[id]=true;
    persist();
    updateRequirements();
  }
  function updateRequirements(){
    var nodes=[].slice.call(document.querySelectorAll("[data-requirement]"));
    nodes.forEach(function(node){node.classList.toggle("done",!!saved.requirements[node.dataset.requirement]);});
    var complete=nodes.length>0&&nodes.every(function(node){return saved.requirements[node.dataset.requirement];});
    var status=document.querySelector("[data-completion-status]");
    var button=document.querySelector("[data-complete]");
    if(status)status.textContent=complete?"All required evidence is complete. You may mark this lesson complete.":"Complete each required interaction and work product. Scrolling alone does not count.";
    if(button){button.disabled=!complete;button.textContent=saved.completed?"Lesson complete":"Mark lesson complete";}
  }
  function setLens(name){
    body.dataset.lens=name;
    saved.lens=name;
    document.querySelectorAll("[data-lens]").forEach(function(button){
      var on=button.dataset.lens===name;
      button.classList.toggle("on",on);
      button.setAttribute("aria-selected",String(on));
    });
    persist();
  }
  document.querySelectorAll("[data-lens]").forEach(function(button){
    button.addEventListener("click",function(){setLens(button.dataset.lens);});
  });
  setLens(saved.lens||"foundation");

  var tooltip=document.getElementById("tt");
  document.querySelectorAll(".term").forEach(function(term){
    function show(){
      if(!tooltip)return;
      tooltip.innerHTML="<b>"+term.textContent+"</b>"+term.dataset.def;
      var rect=term.getBoundingClientRect();
      tooltip.style.left=Math.max(8,Math.min(window.innerWidth-320,rect.left))+"px";
      tooltip.style.top=Math.min(window.innerHeight-100,rect.bottom+8)+"px";
      tooltip.style.opacity="1";
    }
    function hide(){if(tooltip)tooltip.style.opacity="0";}
    term.addEventListener("mouseenter",show);term.addEventListener("focus",show);
    term.addEventListener("mouseleave",hide);term.addEventListener("blur",hide);
    term.setAttribute("tabindex","0");
  });

  var lastTrigger=null;
  function openDrawer(id,trigger){
    var drawer=document.getElementById(id),scrim=document.querySelector(".drawer-scrim");
    if(!drawer)return;
    lastTrigger=trigger||document.activeElement;
    document.querySelectorAll(".drawer.open").forEach(function(item){item.classList.remove("open");item.setAttribute("aria-hidden","true");});
    drawer.classList.add("open");drawer.setAttribute("aria-hidden","false");
    if(scrim)scrim.classList.add("open");
    body.classList.add("locked");
    var close=drawer.querySelector("[data-close-drawer]");if(close)close.focus();
  }
  function closeDrawers(){
    document.querySelectorAll(".drawer.open").forEach(function(drawer){drawer.classList.remove("open");drawer.setAttribute("aria-hidden","true");});
    var scrim=document.querySelector(".drawer-scrim");if(scrim)scrim.classList.remove("open");
    body.classList.remove("locked");
    if(lastTrigger&&lastTrigger.focus)lastTrigger.focus();
  }
  document.querySelectorAll("[data-open-graph]").forEach(function(button){button.onclick=function(){openDrawer("graphDrawer",button);};});
  document.querySelectorAll("[data-open-community]").forEach(function(button){button.onclick=function(){openDrawer("communityDrawer",button);};});
  document.querySelectorAll("[data-close-drawer],.drawer-scrim").forEach(function(button){button.onclick=closeDrawers;});
  document.addEventListener("keydown",function(event){if(event.key==="Escape")closeDrawers();});
  document.querySelectorAll("[data-start]").forEach(function(link){link.onclick=function(){mark("started");};});

  document.querySelectorAll("[data-record]").forEach(function(button){
    button.onclick=function(){
      var card=button.closest(".record");card.classList.toggle("selected");
      button.setAttribute("aria-pressed",String(card.classList.contains("selected")));
      var selected=document.querySelectorAll(".record.selected").length;
      var feedback=document.querySelector("[data-record-feedback]");
      if(feedback){
        feedback.className="feedback show "+(selected>=2?"good":"");
        feedback.textContent=selected>=2?"Good. The answer needs records and named relationships across systems.":"Select at least two records that must connect.";
      }
      if(selected>=2)mark("opening");
    };
  });

  var triple=document.querySelector("[data-triple-builder]");
  if(triple){
    var selects=[].slice.call(triple.querySelectorAll("select"));
    function renderTriple(){
      var values=selects.map(function(select){return select.value;});
      var output=triple.querySelector("[data-triple-output]");
      output.textContent=values.every(Boolean)?values.join(" -> "):"Choose all three parts.";
    }
    selects.forEach(function(select){select.addEventListener("change",renderTriple);});
    triple.querySelector("[data-check-triple]").onclick=function(){
      var values=selects.map(function(select){return select.value;});
      var correct=values[0]==="Pump_P104"&&values[1]==="serves"&&values[2]==="Pressure_Zone_3";
      var feedback=triple.querySelector(".feedback");
      feedback.className="feedback show "+(correct?"good":"bad");
      feedback.textContent=correct?"Correct. Read it aloud: Pump P-104 serves Pressure Zone 3. Direction and relationship are explicit.":"Try again. The pump is the thing being described, serves is the relationship, and the pressure zone is on the other side.";
      if(correct)mark(triple.dataset.required);
    };
    renderTriple();
  }

  document.querySelectorAll("[data-stepper]").forEach(function(root){
    var steps=[].slice.call(root.querySelectorAll(".step")),index=0,timer=null,meter=root.querySelector(".meter i");
    function paint(next){
      index=Math.max(0,Math.min(steps.length-1,next));
      steps.forEach(function(step,i){step.classList.toggle("active",i===index);});
      if(meter)meter.style.width=((index+1)/steps.length*100)+"%";
      root.querySelectorAll("[data-step-index]").forEach(function(button){button.classList.toggle("primary",Number(button.dataset.stepIndex)===index);});
      if(index===steps.length-1)mark(root.dataset.required);
    }
    function stop(){if(timer){clearInterval(timer);timer=null;}}
    var back=root.querySelector("[data-back]"),next=root.querySelector("[data-next]"),play=root.querySelector("[data-play]"),pause=root.querySelector("[data-pause]"),reset=root.querySelector("[data-reset]");
    if(back)back.onclick=function(){stop();paint(index-1);};
    if(next)next.onclick=function(){stop();paint(index+1);};
    if(play)play.onclick=function(){stop();if(index===steps.length-1)paint(0);timer=setInterval(function(){if(index===steps.length-1){stop();return;}paint(index+1);},1600);};
    if(pause)pause.onclick=stop;
    if(reset)reset.onclick=function(){stop();paint(0);};
    root.querySelectorAll("[data-step-index]").forEach(function(button){button.onclick=function(){stop();paint(Number(button.dataset.stepIndex));};});
    paint(0);
  });

  document.querySelectorAll("[data-stack]").forEach(function(root){
    var detail=root.querySelector("[data-stack-detail]");
    root.querySelectorAll("[data-stack-item]").forEach(function(button){
      button.onclick=function(){
        root.querySelectorAll("[data-stack-item]").forEach(function(item){item.classList.toggle("on",item===button);});
        detail.innerHTML="<h3>"+button.dataset.title+"</h3><p>"+button.dataset.copy+"</p><p><b>Utility example:</b> "+button.dataset.example+"</p>";
        mark(root.dataset.required);
      };
    });
  });

  document.querySelectorAll("[data-quiz]").forEach(function(quiz){
    var choices=[].slice.call(quiz.querySelectorAll("[data-correct]"));
    var multiple=quiz.dataset.mode==="multi";
    choices.forEach(function(choice){
      choice.onclick=function(){
        if(multiple){choice.classList.toggle("selected");}
        else{choices.forEach(function(item){item.classList.remove("selected");});choice.classList.add("selected");}
      };
    });
    var check=quiz.querySelector("[data-check-quiz]");
    if(check)check.onclick=function(){
      var ok=true,selectedCount=0;
      choices.forEach(function(choice){
        var selected=choice.classList.contains("selected"),wanted=choice.dataset.correct==="1";
        if(selected)selectedCount++;
        choice.classList.remove("correct","wrong");
        if(wanted)choice.classList.add("correct");
        if(selected&&!wanted)choice.classList.add("wrong");
        if(selected!==wanted)ok=false;
      });
      if(!multiple&&selectedCount!==1)ok=false;
      var feedback=quiz.querySelector(".feedback");
      feedback.className="feedback show "+(ok?"good":"bad");
      feedback.textContent=ok?quiz.dataset.pass:(quiz.dataset.retry||"Review the highlighted choices and try again.");
      if(ok)mark(quiz.dataset.required);
    };
  });

  document.querySelectorAll("[data-match]").forEach(function(quiz){
    var check=quiz.querySelector("[data-check-match]");
    check.onclick=function(){
      var fields=[].slice.call(quiz.querySelectorAll("select[data-answer]"));
      var correct=0;
      fields.forEach(function(field){
        var ok=field.value===field.dataset.answer;
        field.style.borderColor=ok?"#087a55":"#b73535";
        if(ok)correct++;
      });
      var passed=correct===fields.length,feedback=quiz.querySelector(".feedback");
      feedback.className="feedback show "+(passed?"good":"bad");
      feedback.textContent=passed?quiz.dataset.pass:correct+" of "+fields.length+" are correct. Use the job each standard performs and try again.";
      if(passed)mark(quiz.dataset.required);
    };
  });

  document.querySelectorAll("[data-sorter]").forEach(function(sorter){
    sorter.querySelector("[data-check-sorter]").onclick=function(){
      var fields=[].slice.call(sorter.querySelectorAll("select[data-answer]")),correct=0;
      fields.forEach(function(field){
        var ok=field.value===field.dataset.answer;
        field.style.borderColor=ok?"#087a55":"#b73535";
        if(ok)correct++;
      });
      var passed=correct===fields.length,feedback=sorter.querySelector(".feedback");
      feedback.className="feedback show "+(passed?"good":"bad");
      feedback.textContent=passed?"All artifacts are assigned by their primary job in this scenario.":correct+" of "+fields.length+" are correct. Ask what question the artifact primarily answers.";
      if(passed)mark(sorter.dataset.required);
    };
  });

  document.querySelectorAll("[data-failure-lab]").forEach(function(lab){
    var result=lab.querySelector("[data-failure-result]");
    lab.querySelectorAll("[data-failure]").forEach(function(button){
      button.onclick=function(){
        lab.querySelectorAll("[data-failure]").forEach(function(item){item.classList.toggle("primary",item===button);});
        result.innerHTML="<h3>"+button.dataset.title+"</h3><p>"+button.dataset.result+"</p><p><b>Repair:</b> "+button.dataset.repair+"</p>";
        mark(lab.dataset.required);
      };
    });
  });

  document.querySelectorAll("form[data-artifact]").forEach(function(form){
    var preview=form.closest(".artifact").querySelector("[data-artifact-preview]");
    var fields=[].slice.call(form.querySelectorAll("input,textarea,select"));
    if(saved.artifact&&saved.artifact[form.dataset.artifact]){
      fields.forEach(function(field,i){field.value=saved.artifact[form.dataset.artifact][i]||"";});
    }
    function render(){
      preview.textContent=fields.map(function(field){
        return (field.dataset.label||field.name).toUpperCase()+"\n"+(field.value.trim()||"[Complete this field]");
      }).join("\n\n");
    }
    fields.forEach(function(field){field.addEventListener("input",render);});
    form.onsubmit=function(event){
      event.preventDefault();
      var valid=fields.every(function(field){return field.value.trim().length>=3;});
      var feedback=form.querySelector(".feedback");
      feedback.className="feedback show "+(valid?"good":"bad");
      feedback.textContent=valid?"Saved in this browser as a working draft. Review it with the named utility owner.":"Complete every field with a specific statement.";
      if(valid){
        saved.artifact[form.dataset.artifact]=fields.map(function(field){return field.value;});
        mark(form.dataset.required);
        persist();
      }
    };
    render();
  });

  var complete=document.querySelector("[data-complete]");
  if(complete)complete.onclick=function(){
    saved.completed=true;persist();updateRequirements();announce("Lesson completion recorded in this browser. Production learner records remain disabled.","good");
  };
  window.addEventListener("scroll",function(){
    var max=document.documentElement.scrollHeight-document.documentElement.clientHeight;
    var bar=document.querySelector(".reading");
    if(bar)bar.style.width=(max?document.documentElement.scrollTop/max*100:0)+"%";
  });
  updateRequirements();
})();
