function showData(data){
	if(data)
	{
		document.getElementById('reez').innerHTML = '<td></td>';
		$.each(data, function(index) {
			var table = document.getElementById("reez");
			var row = table.insertRow(0);
		    var cell1 = row.insertCell(0);
		    cell1.innerHTML = data[index].insulin;
    		cell1.innerHTML = data[index].food;
       });
	}else{
		document.getElementById('reez').innerHTML = '<td>Ooops no results</td>';
	}
}

function handleClick(e){
	var text = $('#txtDate').val();
	$.ajax('/', {
		type: 'GET',
		data: {
			fmt: text
		},
		success:showData
	});
}

function post_entry(e){
	var blood_sugar = $('#blood_sugar').val();
	var insulin = $('#insulin').val();
	var food = $('#food').val();
	var date_entry = $('#txtDate').val();
	$.ajax('/', {
		type: 'POST',
		data: {
			blood_sugar: blood_sugar,
			insulin: insulin,
			food: food,
			date_entry: date_entry
		},
		success:function(returndatafromserver){
         	handleClick(returndatafromserver)
         }
	});
}

$(document).ready(function(){
	$('#post_entry').on('click', post_entry);
});
$(document).ready(function(){
	$('#getitButton').on('click', handleClick);
});


function getdate_back() {


    var tt = document.getElementById('txtDate').value;
    var date = new Date(tt);
    var newdate = new Date(date);

    newdate.setDate(newdate.getDate() - 1);
    
    var dd = newdate.getDate();
    var mm = newdate.getMonth() + 1;
    var y = newdate.getFullYear();

    if(dd<10) {
		    dd='0'+dd
		} 
		if(mm<10) {
		    mm='0'+mm
		} 
    var someFormattedDate = mm + '/' + dd + '/' + y;
    document.getElementById('txtDate').value = someFormattedDate;
    handleClick()
}

function getdate_forward() {


    var tt = document.getElementById('txtDate').value;
    var date = new Date(tt);
    var newdate = new Date(date);

    newdate.setDate(newdate.getDate() + 1);
    
    var dd = newdate.getDate();
    var mm = newdate.getMonth() + 1;
    var y = newdate.getFullYear();

    if(dd<10) {
		    dd='0'+dd
		} 

		if(mm<10) {
		    mm='0'+mm
		} 

    var someFormattedDate = mm + '/' + dd + '/' + y;
    document.getElementById('txtDate').value = someFormattedDate;
    handleClick()
}

$(window).load(function(){
	var today = new Date();
		var dd = today.getDate();
		var mm = today.getMonth()+1; //January is 0!
		var yyyy = today.getFullYear();

		if(dd<10) {
		    dd='0'+dd
		} 

		if(mm<10) {
		    mm='0'+mm
		} 

		today = mm+'/'+dd+'/'+yyyy;

		document.getElementById('txtDate').value = today;
		handleClick()
})