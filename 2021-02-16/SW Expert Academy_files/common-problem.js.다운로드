function checkIsFirstOpen(contestProbId, categoryId, categoryType)
{
	var checkParams =
	{
		contestProbId : contestProbId,
		categoryId : categoryId,
		categoryType : categoryType
	};

	var checkUrl = contextPath + "/contestHistory/checkIsFirstOpen.do";
	$.ajax(
	{
		type : "POST",
		url : checkUrl,
		data : checkParams,
		async: false,
		success : function(ret)
		{
			if(ret.probOpenYn == 'N') {
				saveFirstOpenHistory(contestProbId, categoryId, categoryType);
			} 
		},
		error : function(request, err, ex)
		{
			var errorMsg = err + " ===> " + ex;
			doAlert(errorMsg, function() {
			});
		}
	});
	
}

function saveFirstOpenHistory(contestProbId, categoryId, categoryType)
{
	var saveParams =
	{
		contestProbId : contestProbId,
		categoryId : categoryId,
		categoryType : categoryType,
		solveStatusCd : "V"
	};

	var saveUrl = contextPath + "/contestHistory/insertFirstOpenProbHistory.do";
	$.ajax(
	{
		type : "POST",
		url : saveUrl,
		data : saveParams,
		async: false,
		success : function(ret)
		{
		},
		error : function(request, err, ex)
		{
			var errorMsg = err + " ===> " + ex;
			doAlert(errorMsg, function() {
			});
		}
	});
}

function fnGoProblemTest(contestProbId, categoryId, categoryType)
{
	var params = {
			contestProbId : contestProbId,
			categoryId : categoryId,
			categoryType : categoryType
	};
	var dateString = new Date();
	var url = contextPath + '/solvingProblem/solvingProblem.do';
	var args = {
			actionUri : url,
			formData : params,
			target : 'problem'
	};
	fn_open_page_window( args);
}


function fnGoProblemDetail(contestProbId, categoryId, categoryType, url)
{
	var params = {
			contestProbId : contestProbId,
			categoryId : categoryId,
			categoryType : categoryType
	};
	var args = {
			actionUri : url,
			formData : params 
	};
	fn_open_page_get( args );
}

function fnCheckAndGoCodeDetail(contestHistoryId, fCallback)
{
	var checkParams = { contestHistoryId : contestHistoryId};
	var checkUrl = contextPath + "/contestHistory/checkIsFirstOpenCode.do";
	$.ajax(
	{
		type : "POST",
		url : checkUrl,
		data : checkParams,
		dataType: 'json',
		async: false,
		success : function(ret)
		{
			if(ret.message ==  "Success"){
				if(ret.data > 0){
					var msg  = '코드 열람시 활동점수 @Point@점이 차감됩니다.<br>코드를 보시겠습니까?'.replace("@Point@", ret.data);
					doConfirm(msg, function(result) {
						if(result){
							fCallback(contestHistoryId);
						}
					});
				}
				else{
					fCallback(contestHistoryId);
				}
			}
			else {
				var msg = '활동포인트가 부족하여 코드보기가 불가합니다.\n문제풀이, 학습, Talk등을 통해 활동포인트를 취득한 후 코드보기를 이용할 수 있습니다.';
				doAlert(msg, function() {});
			}
		},
		error : function(request, err, ex)
		{
			var errorMsg = err + " ===> " + ex;
			doAlert(errorMsg, function() {
			});
		}
	});
}
