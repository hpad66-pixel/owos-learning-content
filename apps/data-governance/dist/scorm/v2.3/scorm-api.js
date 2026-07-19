(function (global) {
  function findApi(win) {
    var attempts = 0;
    while (win && !win.API && win.parent && win.parent !== win && attempts < 20) {
      attempts += 1;
      win = win.parent;
    }
    return win && win.API ? win.API : null;
  }

  global.APAS_SCORM = {
    initializeAndComplete: function () {
      var api = findApi(global);
      if (!api) return false;
      api.LMSInitialize("");
      api.LMSSetValue("cmi.core.lesson_status", "completed");
      api.LMSCommit("");
      return true;
    }
  };
})(window);
