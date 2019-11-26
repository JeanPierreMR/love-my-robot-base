const $tableID = $('#table');
 const $BTN = $('#export-btn');
 const $EXPORT = $('#export');

 const newTr = `
<tr class="hide">
  <td class="pt-3-half" contenteditable="true">`
  const otr =`</td>
  <td class="pt-3-half" contenteditable="true">`
  const terc =`</td>


  <td>
    <span class="table-remove"><button type="button" class="btn btn-danger btn-rounded btn-sm my-0 waves-effect waves-light">Remove</button></span>
  </td>
</tr>`;
 function add(data, data1){
    $('tbody').append(newTr+data+otr+data1+terc);
 }
//FUNCION RECORRER
function recorrido(){

    var table = document.getElementById("table");
    var codigojunto=``;

    for (var i = 1, row; row = table.rows[i]; i++) {
        //iterate through rows
        for (var j = 0, col; col = row.cells[j]; j++) {
            //iterate through columns
            if(col.innerText === "Remove"){

            }else{
            codigojunto = codigojunto +" "+ col.innerText;
            }
        }  
        codigojunto = codigojunto + "\n"
    }
    var doc = prompt(codigojunto); 
    

    var http = new XMLHttpRequest();
    var url = 'http://localhost:3000';
    var params = codigojunto;
    http.open('POST', url, true);

    //Send the proper header information along with the request
    http.setRequestHeader('Content-type', 'application/string');

    http.onreadystatechange = function() {//Call a function when the state changes.
        if(http.readyState == 4 && http.status == 200) {
            alert(http.responseText);
        }
    }
    http.send(params);
}


 $tableID.on('click', '.table-remove', function () {

   $(this).parents('tr').detach();
 });

 $tableID.on('click', '.table-up', function () {

   const $row = $(this).parents('tr');

   if ($row.index() === 1) {
     return;
   }

   $row.prev().before($row.get(0));
 });

 $tableID.on('click', '.table-down', function () {

   const $row = $(this).parents('tr');
   $row.next().after($row.get(0));
 });

 // A few jQuery helpers for exporting only
 jQuery.fn.pop = [].pop;
 jQuery.fn.shift = [].shift;

 $BTN.on('click', () => {

   const $rows = $tableID.find('tr:not(:hidden)');
   const headers = [];
   const data = [];

   // Get the headers (add special header logic here)
   $($rows.shift()).find('th:not(:empty)').each(function () {

     headers.push($(this).text().toLowerCase());
   });

   // Turn all existing rows into a loopable array
   $rows.each(function () {
     const $td = $(this).find('td');
     const h = {};

     // Use the headers from earlier to name our hash keys
     headers.forEach((header, i) => {

       h[header] = $td.eq(i).text();
     });

     data.push(h);
   });

   // Output the result
   $EXPORT.text(JSON.stringify(data));
 });