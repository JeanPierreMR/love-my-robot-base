const $tableID = $('#table');
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
    //loops through table obtaining content and posting it
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
    $.post('/load_code', { lmr: codigojunto })
    alert("listo");
}


 $tableID.on('click', '.table-remove', function () {

   $(this).parents('tr').detach();
 });

