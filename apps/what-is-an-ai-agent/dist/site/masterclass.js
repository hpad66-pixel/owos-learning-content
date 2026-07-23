(function(){
"use strict";
var body=document.body,moduleId=body.dataset.module||"00",key="owos:aia001:"+moduleId+":master:v1",saved={};
try{saved=JSON.parse(localStorage.getItem(key)||"{}");}catch(error){}
var instructorNotes={
"01":{
title:"Do not buy the label. Inspect the behavior.",
intro:[
"Let us slow this down because this first distinction prevents a great deal of expensive confusion. A polished chat window can feel intelligent, but appearance does not tell you what the system is responsible for. The useful questions are operational. What information can it reach? Can it remember where a task stands? Can it choose between approved next steps? Can it act through another system? Who must approve the result?",
"Picture a maintenance supervisor asking which work orders need attention before the morning shift. A chatbot may explain prioritization. Retrieval may find the work orders and cite them. A fixed workflow may sort them using stable priority rules. A bounded agent may notice missing evidence, retrieve it from an approved source, compare the records, prepare a recommendation, and stop for the supervisor. Those are different jobs with different risks."
],
steps:[["Question","Name the utility job in ordinary language."],["Evidence","Identify the records needed to answer it."],["Behavior","Observe what the system can choose and do."],["Architecture","Use the simplest system that completes the job safely."]],
visual:"Read the capability ladder as added responsibility, not as a ranking of better technology. Each step should earn its place by solving a problem the simpler step cannot solve. The final blue block is darker because the responsibility is greater, not because it is automatically the preferred answer.",
activity:"As you test the capability builder, listen for the moment the system changes category. Retrieval adds evidence. Fixed rules add predictable routing. Tools, task state, bounded choice, and stop conditions create the operating pattern we call an agent. If your problem does not need those responsibilities, do not add them.",
artifact:"Your field card is a meeting tool. Write it so a supervisor, engineer, procurement lead, or vendor can use the same questions. A good card replaces vague claims with observable evidence and gives the organization a defensible reason for choosing one architecture over another."
},
"02":{
title:"An agent is a loop with brakes, not a single clever answer.",
intro:[
"The easiest way to understand an agent is to stop thinking about the final sentence and watch the work that happens before it. The loop begins with a measurable goal. It selects one approved next step, uses a permitted tool, records what happened, evaluates the result, and decides whether to continue, adjust, stop, or ask a person for help.",
"In utility work, the brakes matter as much as the motion. A missing maintenance record cannot be wished away. A failed connector cannot be retried forever. A recommendation cannot quietly become an operating command. The loop must carry limits, evidence, cost, and a named human handoff at every turn."
],
steps:[["Goal","Define the result and required evidence."],["Act","Use one approved tool for one bounded step."],["Observe","Record the source, time, result, and limitation."],["Control","Stop, retry within limits, or escalate to a person."]],
visual:"Follow the loop clockwise, but keep your eye on the control decision in the center. That center is where the system proves it is governed. It does not continue because the language sounds confident. It continues only when the recorded result supports the next step.",
activity:"Run the simulation one step at a time before using Play. At each stop, ask what became known and what remains uncertain. If you cannot explain why the next step is allowed, the loop is moving without enough control.",
artifact:"The loop trace is the record another person can inspect after the fact. Make the goal measurable, name the tools precisely, and write stop conditions that can be tested. A useful trace lets a reviewer reconstruct the work without guessing what the system might have done."
},
"03":{
title:"The anatomy only works when the parts agree.",
intro:[
"An agent is not one model wearing a larger name. It is a working arrangement of a goal, evidence, instructions, tools, task state, evaluation, permissions, and human authority. Remove one part and the failure often appears somewhere else. Weak identity can make good records look unrelated. Weak evaluation can let an unsupported result pass. Excessive permission can turn a drafting error into an operational consequence.",
"Think about a lift-station briefing. The model may write clearly, but clarity does not confirm the asset identity, the age of the alarm, or the status of the last work order. The anatomy diagram helps you see which component owns each responsibility so the organization can test the whole system instead of admiring one output."
],
steps:[["Sense","Bring in approved evidence with identity and time."],["Reason","Compare the evidence with the goal and rules."],["Remember","Keep task state, attempts, and open questions."],["Act safely","Use least authority and preserve the human decision."]],
visual:"Read the anatomy from the outside toward the decision. Sources and tools connect the agent to the utility. State and evaluation keep the work coherent. Permissions and human authority define what may happen next. The model supports the process, but it does not own the operating decision.",
activity:"Use the anatomy lab to remove or weaken one component. Notice that the visible failure may occur downstream from the missing part. This is why an agent review should test relationships between components, not simply test whether each component exists.",
artifact:"Your anatomy map should be specific enough for a technical lead and an operating owner to review together. Name real source classes, real tool boundaries, the state that must persist, and the person who accepts the result. General labels hide risk."
},
"04":{
title:"A handoff is a transfer of responsibility, evidence, and authority.",
intro:[
"A multi-agent design can look efficient on a diagram because the arrows are clean. Real work is less forgiving. The receiving role needs to know what was requested, what evidence was used, what remains uncertain, what actions were permitted, and which person owns the next decision. Without that contract, one agent can pass confidence while dropping context.",
"The utility example in this lesson is intentionally ordinary. Records are gathered, conflicts are checked, a recommendation is drafted, and a human reviewer decides. That ordinary sequence exposes the important issue: every transfer must preserve enough evidence and authority for the next role to act responsibly."
],
steps:[["Package","State the task, evidence, limits, and open questions."],["Transfer","Send it to a named role through an approved path."],["Accept","Validate identity, completeness, and authority."],["Close","Record the outcome or return it with a clear reason."]],
visual:"Read the handoff diagram by following the evidence, not merely the arrow. A successful transfer preserves the source trail and makes the next owner visible. If a receiving agent must infer the goal or search for missing context, the handoff contract is incomplete.",
activity:"As you work through the handoff simulation, watch for three failure points: a vague request, evidence that loses its source, and authority that expands during transfer. Repairing those points is more valuable than adding another agent.",
artifact:"Write the handoff contract as if a new team member must use it tomorrow. Define acceptance tests, rejection reasons, escalation ownership, and the record that proves completion. The contract should reduce ambiguity, not document it."
},
"05":{
title:"Agent, agentic, and automated describe different operating choices.",
intro:[
"These terms are often mixed together, so let us make them useful. Automation means a system follows a defined process. An agent means a bounded system can select among approved next steps while pursuing a goal. Agentic describes the degree to which a larger process uses those goal-directed choices. A process may be partly agentic without handing one system broad authority.",
"For a utility, the important decision is not which word sounds advanced. It is how much variability the task contains, how serious the consequence is, and how much discretion the organization is prepared to govern. Stable billing rules may belong in a deterministic workflow. Research across changing sources may benefit from bounded agency. Chemical-feed control is a different consequence class entirely."
],
steps:[["Stable path","Use rules when the same input should follow the same route."],["Variable evidence","Add retrieval when the answer depends on changing records."],["Bounded choice","Use an agent when the next safe step cannot be fixed in advance."],["Human authority","Keep consequential approval with a named person."]],
visual:"Use the autonomy spectrum as a decision aid, not a maturity model. Moving right adds discretion and control obligations. The correct position is the lowest level that can do the job and produce the required evidence.",
activity:"In the architecture sorter, do not reward the most complicated option. Ask what varies, what must be observed between steps, and what would happen if the system is wrong. A correct choice may be a simple workflow.",
artifact:"Your architecture decision record should make disagreement productive. State why the chosen pattern fits, what alternatives were considered, and which evidence would cause the team to revisit the decision."
},
"06":{
title:"Guardrails are the operating design, not a warning label.",
intro:[
"A sentence that says use responsibly is not a guardrail. A guardrail is a control the system and its owners can actually apply. It may restrict identity, data, tools, permissions, cost, retries, output use, or escalation. Several layers work together because no single control can carry the whole consequence.",
"Start with least authority. If the pilot only needs to read records and draft a recommendation, it should not receive permission to modify records. Then test the boundary. What happens when the source is missing, the identity is uncertain, the tool is unavailable, the cost limit is reached, or the requested action is prohibited?"
],
steps:[["Prevent","Block prohibited data, tools, and actions."],["Detect","Observe failures, drift, cost, and unusual behavior."],["Pause","Stop when evidence or authority is insufficient."],["Escalate","Transfer the decision and evidence to a named person."]],
visual:"Read the guardrail layers from identity outward. The inner layers protect who and what the system is working with. The outer layers control action, monitoring, and human response. A weakness in one layer should be caught by another before it reaches a utility consequence.",
activity:"Use the failure lab to press on the design. A useful test is not whether the happy path works. It is whether the system stops cleanly, explains why, preserves evidence, and reaches the correct human owner when the path breaks.",
artifact:"The guardrail plan is an operating agreement. Write controls in testable language. Name who owns each control, how it is monitored, and what happens after a failure. If a control cannot be tested, it is still an intention."
},
"07":{
title:"The best first use case is valuable, ready, bounded, and owned.",
intro:[
"Utilities can imagine hundreds of agent ideas. The hard work is deciding which one deserves a pilot. Start with a real job and a real owner. Then look at evidence readiness, consequence, review effort, cost, and the simpler alternatives. A high-value idea with poor records is not ready. An easy idea with little value may not deserve automation at all.",
"A good first pilot usually reads before it writes, recommends before it acts, and works in a domain where outcomes can be compared with historical cases. Regulatory research, inspection reconciliation, and work-order preparation can often be bounded this way. Direct operational control cannot be treated as the same kind of experiment."
],
steps:[["Value","Name the decision, delay, error, or effort to improve."],["Readiness","Check sources, identity, ownership, and baseline data."],["Consequence","Define the harm if the result is wrong or late."],["Portfolio choice","Advance, simplify, defer, or reject with reasons."]],
visual:"Read the opportunity map as families of work, not as ready-made products. Each family connects people, records, and consequences differently. The map helps you compare the work before you compare technology.",
activity:"When you sort the proposals, include human review in the cost. A system that saves drafting time but creates more checking, correction, and uncertainty may not improve the operation. The pilot measure must capture the whole job.",
artifact:"The opportunity portfolio should help leaders say yes, not yet, use something simpler, or no. Include the reason for each decision so the next review starts from evidence instead of enthusiasm."
},
"08":{
title:"A pilot earns the next decision. It does not prove the original idea.",
intro:[
"The capstone brings the course together around one discipline: design a small test that can tell the truth. Your pilot should have a measurable goal, approved evidence, bounded tools, explicit prohibitions, historical test cases, cost limits, human review, and a date when the organization decides whether to continue, change, simplify, or stop.",
"Success does not mean the agent survives. If a fixed workflow performs the job more reliably and cheaply, the pilot has succeeded by revealing the better architecture. If the evidence is not ready, the right result may be a data improvement plan. The point is to make a defensible operating decision."
],
steps:[["Frame","Choose one narrow job and establish the current baseline."],["Design","Connect evidence, tools, state, authority, and evaluation."],["Test","Use historical cases, failure cases, and prohibited outcomes."],["Decide","Continue, revise, simplify, or stop using recorded results."]],
visual:"Read the canvas from the problem through the pilot, then inspect it backward. The backward review exposes hidden dependencies. A measure may depend on a source that has no owner. A tool may require a permission the pilot should not have. A handoff may end with nobody accountable.",
activity:"Use the adversarial review as a constructive challenge. Try to break the design before the utility depends on it. Each repair should narrow ambiguity, reduce authority, strengthen evidence, or improve the decision rule.",
artifact:"The final brief should be ready for a cross-functional review. Write it for operations, information technology, security, legal, procurement, and the business owner. Each reader should see the decision they own and the evidence they need."
}
};
function teachingExpansion(){
  var note=instructorNotes[moduleId];
  if(!note)return;
  var artifact=document.querySelector(".artifact,.work");
  if(!artifact)return;
  var host=artifact.closest(".section");
  var section=document.createElement("section");
  section.className="section teaching-bridge";
  section.innerHTML='<span class="tag">Instructor bridge</span><h2>'+note.title+'</h2><div class="instructor-dialogue"><span class="voice">Let us connect the pieces</span><div><p>'+note.intro.join('</p><p>')+'</p></div></div><div class="visual-break"><span class="eyebrow">How the decision moves</span><h3>Read the work from left to right.</h3><p>This graphic turns the lesson into an operating sequence. Each box adds a question that must be answered before responsibility moves forward.</p><div class="concept-flow">'+note.steps.map(function(step,index){return '<article class="concept-step"><span class="number">'+(index+1)+'</span><b>'+step[0]+'</b><small>'+step[1]+'</small></article>';}).join("")+'</div></div><div class="takeaway"><b>What you should be able to say now</b><span>'+note.title+'</span></div>';
  host.insertAdjacentElement("beforebegin",section);
  document.querySelectorAll("figure.visual").forEach(function(visual){
    if(visual.previousElementSibling&&visual.previousElementSibling.classList.contains("instructor-dialogue"))return;
    var guide=document.createElement("div");guide.className="instructor-dialogue";guide.innerHTML='<span class="voice">How to read this graphic</span><div><p>'+note.visual+'</p><p>Pause before moving on and explain the picture in your own words. If you cannot state the relationship it shows, read the labels again and connect them to the utility situation above.</p></div>';visual.insertAdjacentElement("beforebegin",guide);
  });
  document.querySelectorAll("[data-lab],[data-stepper]").forEach(function(activity){
    if(activity.previousElementSibling&&activity.previousElementSibling.classList.contains("instructor-dialogue"))return;
    var guide=document.createElement("div");guide.className="instructor-dialogue";guide.innerHTML='<span class="voice">Before you interact</span><div><p>'+note.activity+'</p><p>Try one choice, read the consequence, then compare it with another. The learning is in the change between the two results, not in clicking every button.</p></div>';activity.insertAdjacentElement("beforebegin",guide);
  });
  if(!artifact.previousElementSibling||!artifact.previousElementSibling.classList.contains("instructor-dialogue")){
    var guide=document.createElement("div");guide.className="instructor-dialogue";guide.innerHTML='<span class="voice">Build something you can use</span><div><p>'+note.artifact+'</p><p>Use specific names, evidence, owners, and limits. You are not completing a form for the course. You are drafting a professional work product that can support a real conversation.</p></div>';artifact.insertAdjacentElement("beforebegin",guide);
  }
}
teachingExpansion();
function persist(){localStorage.setItem(key,JSON.stringify(saved));updateCompletion();}
function mark(id){saved[id]=true;persist();}
function updateCompletion(){var required=[].slice.call(document.querySelectorAll("[data-required]")),done=required.filter(function(el){return el.classList.contains("done")||saved[el.dataset.required];}).length,button=document.querySelector("[data-complete]"),status=document.querySelector("[data-completion-status]");if(button)button.disabled=done<required.length;if(status)status.textContent=done+" of "+required.length+" required learning activities complete.";required.forEach(function(el){if(saved[el.dataset.required])el.classList.add("done");});}
document.querySelectorAll("[data-quiz]").forEach(function(quiz){var id=quiz.dataset.quiz,mode=quiz.dataset.mode||"single",feedback=quiz.querySelector(".feedback");quiz.addEventListener("click",function(event){var choice=event.target.closest(".choice");if(!choice)return;if(mode==="multi")choice.classList.toggle("selected");else{quiz.querySelectorAll(".choice").forEach(function(item){item.classList.remove("selected");});choice.classList.add("selected");}});var check=quiz.querySelector("[data-check]");if(check)check.onclick=function(){var options=[].slice.call(quiz.querySelectorAll(".choice")),ok=true;options.forEach(function(option){var want=option.dataset.correct==="1",got=option.classList.contains("selected");option.classList.remove("correct","wrong");if(want)option.classList.add("correct");if(got&&!want)option.classList.add("wrong");if(want!==got)ok=false;});feedback.classList.add("show");feedback.textContent=ok?quiz.dataset.pass:"Review the highlighted choices and try again. "+(quiz.dataset.retry||"Use the operating rule explained above.");if(ok){quiz.classList.add("done");mark(id);}};});
document.querySelectorAll("[data-match]").forEach(function(quiz){var id=quiz.dataset.match,feedback=quiz.querySelector(".feedback");quiz.querySelector("[data-check]").onclick=function(){var fields=[].slice.call(quiz.querySelectorAll("select[data-answer]")),correct=fields.filter(function(field){var ok=field.value===field.dataset.answer;field.style.borderColor=ok?"#0e8a64":"#c84444";return ok;}).length;feedback.classList.add("show");feedback.textContent=correct===fields.length?quiz.dataset.pass:correct+" of "+fields.length+" matches are correct. Read each plain-English definition and try again.";if(correct===fields.length){quiz.classList.add("done");mark(id);}};});
document.querySelectorAll("[data-stepper]").forEach(function(root){var id=root.dataset.stepper,steps=[].slice.call(root.querySelectorAll(".step")),buttons=[].slice.call(root.querySelectorAll(".stepnav button")),index=0,timer=null,meter=root.querySelector(".meter i");function paint(i){index=Math.max(0,Math.min(steps.length-1,i));steps.forEach(function(step,j){step.classList.toggle("active",j===index);});buttons.forEach(function(button,j){button.classList.toggle("active",j===index);});meter.style.width=((index+1)/steps.length*100)+"%";if(index===steps.length-1){root.classList.add("done");mark(id);}}function stop(){if(timer){clearInterval(timer);timer=null;}}buttons.forEach(function(button,i){button.onclick=function(){stop();paint(i);};});var back=root.querySelector("[data-back]"),next=root.querySelector("[data-next]"),play=root.querySelector("[data-play]"),pause=root.querySelector("[data-pause]"),reset=root.querySelector("[data-reset]");if(back)back.onclick=function(){stop();paint(index-1);};if(next)next.onclick=function(){stop();paint(index+1);};if(play)play.onclick=function(){stop();if(index===steps.length-1)paint(0);timer=setInterval(function(){if(index===steps.length-1){stop();return;}paint(index+1);},1800);};if(pause)pause.onclick=stop;if(reset)reset.onclick=function(){stop();paint(0);};paint(0);});
document.querySelectorAll("[data-lab]").forEach(function(lab){var id=lab.dataset.lab,result=lab.querySelector(".labresult");lab.querySelectorAll("[data-lab-option]").forEach(function(button){button.onclick=function(){lab.querySelectorAll("[data-lab-option]").forEach(function(item){item.classList.toggle("on",item===button);});result.innerHTML="<h3>"+button.dataset.title+"</h3><p>"+button.dataset.result+"</p>";if(button.dataset.complete==="1"){lab.classList.add("done");mark(id);}};});});
document.querySelectorAll("form[data-artifact]").forEach(function(form){var id=form.dataset.artifact,preview=form.closest(".artifact").querySelector("pre"),fields=[].slice.call(form.querySelectorAll("input,textarea,select"));function text(){return fields.map(function(field){return (field.dataset.label||field.previousSibling.textContent||field.name).trim().toUpperCase()+"\n"+(field.value.trim()||"[Complete]");}).join("\n\n");}function render(){preview.textContent=text();}fields.forEach(function(field){field.addEventListener("input",render);});form.onsubmit=function(event){event.preventDefault();var valid=fields.every(function(field){return field.value.trim().length>2;});var feedback=form.querySelector(".feedback");feedback.classList.add("show");feedback.textContent=valid?"Saved in this browser as a professional draft. Review it with the named utility owner.":"Complete every field with a specific, testable statement.";if(valid){saved[id+"-data"]=fields.map(function(field){return field.value;});form.closest(".artifact").classList.add("done");mark(id);}};if(saved[id+"-data"])fields.forEach(function(field,i){field.value=saved[id+"-data"][i]||"";});render();});
document.querySelectorAll("[data-open-graph]").forEach(function(button){button.onclick=function(){var drawer=document.querySelector(".drawer"),scrim=document.querySelector(".scrim");if(!drawer){var nativeTrigger=document.getElementById("openGraphTop")||document.getElementById("openGraphHero");if(nativeTrigger)nativeTrigger.click();return;}drawer.classList.add("open");scrim.classList.add("open");drawer.setAttribute("aria-hidden","false");drawer.querySelector("[data-close-graph]").focus();};});function closeGraph(){var drawer=document.querySelector(".drawer"),scrim=document.querySelector(".scrim");if(drawer){drawer.classList.remove("open");scrim.classList.remove("open");drawer.setAttribute("aria-hidden","true");}}var close=document.querySelector("[data-close-graph]"),scrim=document.querySelector(".scrim");if(close)close.onclick=closeGraph;if(scrim)scrim.onclick=closeGraph;document.addEventListener("keydown",function(event){if(event.key==="Escape")closeGraph();});
var complete=document.querySelector("[data-complete]");if(complete)complete.onclick=function(){this.textContent="Module complete";saved.completed=true;persist();};
window.addEventListener("scroll",function(){var root=document.documentElement,max=root.scrollHeight-root.clientHeight,bar=document.querySelector(".reading");if(bar)bar.style.width=(max?root.scrollTop/max*100:0)+"%";});updateCompletion();
})();
