(function (root, factory) {
	"use strict";
  if (typeof define === "function" && define.amd) {
    // AMD.
    define(["jquery"], factory);
  } else if (typeof exports === "object") {
    // Node.CommonJS
    if (typeof $ === "undefined") {
      module.exports = factory(require("jquery"));
    } else {
      module.exports = factory($); // jshint ignore:line
    }
  } else {
    // Browser globals (root is window)
    root.hkcommonbox = factory(root.jQuery);
  }
}(this, function init($, undefined) {
	"use strict";
	
	var alretTemplate = '<div class="popup_layer">'+
												'<div class="layer_alert md" style="width: 430px;">' +
													'<p class="txt" style="overflow-y:auto; max-height: 250px;"></p>' +
													'<div class="btn_center">' + 
														'<a class="btn_blue md btn" style="cursor:pointer">확인</a>'+
													'</div>' + 
													'<a class="btn_close" style="cursor:pointer">' + 
														'<span class="hide">닫기</span>' + 
													'</a>' + 
												'</div>' +
											'</div>';
	
	var confirmTemplate = '<div class="popup_layer">'+
													'<div class="layer_alert" style="width: 430px;">'+
														'<p class="txt" style="overflow-y:auto; max-height: 250px;"></p>'+
														'<div class="btn_center">'+
															'<a class="btn_blue sm btn" style="cursor:pointer">확인</a>'+
															'<a class="btn_line sm btn" style="cursor:pointer">취소</a>'+
														'</div>'+
														'<a class="btn_close" style="cursor:pointer">'+
															'<span class="hide">닫기</span>'+
														'</a>'+
													'</div>'+
												'</div>';
	
	var exports = {};
	
	function processCallback(e, dialog, callback) {
		e.stopPropagation();
		e.preventDefault();
		var preserveDialog = $.isFunction(callback) && callback.call(dialog, e) === false;
		if(!preserveDialog) {
			dialog.modal("hide");
		}
	};
	
	function setPosition(dialog) {
		var docWidth = $(document).width();
    var docHeight = $(document).height();
    
    var elWidth = ~~(dialog.children().outerWidth());
    var elHeight = ~~(dialog.children().outerHeight());
    
    if (elHeight < docHeight || elWidth < docWidth) {
    	dialog.css({
    		marginTop: -elHeight / 2,
				marginLeft: -elWidth / 2
			});
		} else {
			dialog.css({top: 0, left: 0});
		}
	};
	
	function setArguments(args, message, callbackfunc) {
		var argn = args.length;
		var message;
		var callbackfunc;
		if(argn < 1 || argn > 2) {
			throw new Error("invalid argument length");
		}
		
		if(typeof args[0] === "string") {
			message = args[0];
		}
		
		if(typeof args[1] === "function" ) {
			callbackfunc = args[1];
		}
		
		return {message:message, callbackfunc:callbackfunc};
	};
	
	exports.confirm = function() {
		var args = arguments;
		var dialog = $(confirmTemplate);
		var message;
		var btnOk = dialog.find(".btn_blue");
		var btnCancel = dialog.find(".btn_line");
		var btnClose = dialog.find(".btn_close");
		var callbackfunc;
		
		var data = setArguments(args);
		message = data.message;
		callbackfunc = data.callbackfunc;
		
		dialog.find(".txt").html(message);
		
		btnOk.callback = function() {
			if ($.isFunction(callbackfunc)) {
				return callbackfunc.call(this, true);
			}
			
			return true;
    };
    
    btnCancel.callback = function() {
    	if($.isFunction(callbackfunc)) {
    		return callbackfunc.call(this, false);
    	}
    	
    	return true;
    }
    
    btnClose.callback = function() {
    	if($.isFunction(callbackfunc)) {
    		return callbackfunc.call(this, false);
    	}
    	return true;
    }
    
    dialog.on("click", ".btn_close", function(e) {
    	processCallback(e, dialog, btnClose.callback);
    });
    
    dialog.on("click", ".btn_line", function(e) {
    	processCallback(e, dialog, btnCancel.callback);
    });
    
    dialog.on("click", ".btn_blue", function(e) {
    	processCallback(e, dialog, btnOk.callback);
    });
    
    dialog.on("shown.bs.modal", function() {
    	dialog.find(".btn_blue").focus();
    });
    
    dialog.on("hidden.bs.modal", function(e) {
    	if(e.target === this) {
    		dialog.remove();
    	}
    });
    
    dialog.modal({backdrop: 'static', keyboard: false});
    dialog.modal("show");
    setPosition(dialog);
    dialog.parent().find('.modal-backdrop').css('z-index', 9998)
    dialog.css('z-index', 9999);
    return dialog;
	}
	
	exports.alert = function() {
		var args = arguments;
		var dialog = $(alretTemplate);
		var btnOk = dialog.find(".btn_blue");
		var btnClose = dialog.find(".btn_close");
		var message;
		var callbackfunc;
		
		var data = setArguments(args);
		message = data.message;
		callbackfunc = data.callbackfunc;
		
		dialog.find(".txt").html(message);
		
		btnOk.callback = function() {
      if ($.isFunction(callbackfunc)) {
        return callbackfunc.call(this, true);
      }
      
      return true;
    };
    
    btnClose.callback = function() {
    	if ($.isFunction(callbackfunc)) {
            return callbackfunc.call(this, true);
          }
    	return true;
    }
		
		dialog.on("click", ".btn_close", function(e) {
    	processCallback(e, dialog, btnClose.callback);
    });
    
    dialog.on("click", ".btn_blue", function(e) {
    	processCallback(e, dialog, btnOk.callback);
    });
    
//    setPosition(dialog);
    
    dialog.on("shown.bs.modal", function() {
    	dialog.find(".btn_blue").focus();
    });
    
    dialog.on("hidden.bs.modal", function(e) {
    	if(e.target === this) {
    		dialog.remove();
    	}
    });
    
    dialog.modal({backdrop: 'static', keyboard: false});
    dialog.modal("show");
    setPosition(dialog);
    dialog.parent().find('.modal-backdrop').css('z-index', 9998).css('opacity', 0);
    dialog.css('z-index', 9999);
    return dialog;
	}
	
	exports.init = function(_$) {
		return init(_$ || $);
	}
	
	return exports;
}));