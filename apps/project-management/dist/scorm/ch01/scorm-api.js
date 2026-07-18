/* Minimal SCORM 1.2 runtime wrapper for One Water OS Academy modules.
   Finds the LMS API if the page is launched inside a SCORM-compliant LMS,
   reports the module as completed when the learner reaches the bottom, and
   does nothing (fails gracefully) when opened as a plain web page. */
(function () {
  "use strict";
  var API = null, ready = false;

  function findAPI(win) {
    var tries = 0;
    while (win.API == null && win.parent != null && win.parent != win && tries < 15) {
      tries++; win = win.parent;
    }
    return win.API;
  }
  function getAPI() {
    var a = findAPI(window);
    if (a == null && window.opener != null) a = findAPI(window.opener);
    return a;
  }

  function init() {
    API = getAPI();
    if (!API) return;
    try {
      API.LMSInitialize("");
      var status = API.LMSGetValue("cmi.core.lesson_status");
      if (status === "" || status === "not attempted" || status === "unknown") {
        API.LMSSetValue("cmi.core.lesson_status", "incomplete");
      }
      API.LMSCommit("");
      ready = true;
    } catch (e) { /* ignore */ }
  }
  function complete() {
    if (!API || !ready) return;
    try {
      API.LMSSetValue("cmi.core.lesson_status", "completed");
      API.LMSSetValue("cmi.core.score.raw", "100");
      API.LMSSetValue("cmi.core.score.min", "0");
      API.LMSSetValue("cmi.core.score.max", "100");
      API.LMSCommit("");
    } catch (e) { /* ignore */ }
  }
  function finish() {
    if (!API || !ready) return;
    try { API.LMSFinish(""); } catch (e) { /* ignore */ }
  }

  window.addEventListener("load", function () {
    init();
    var done = false;
    window.addEventListener("scroll", function () {
      if (done) return;
      if (window.innerHeight + window.scrollY >= document.body.scrollHeight - 80) {
        done = true; complete();
      }
    }, { passive: true });
  });
  window.addEventListener("beforeunload", finish);
})();
