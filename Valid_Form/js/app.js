/*console.log("Estamos Conectados");
document.write("<h1> ALERTA DESDE JS </h1>");
alert("!!!! DANGER ¡¡¡¡")*/
var nt1 = 0.5;
var nt2 = 0.5;
var nt3 = 0.0;
var sum = (nt1+nt2+nt3);
var prom = sum /3;
var sw = 0;
/*console.log("La suma de sus notas es: ",sum/3);
console.log("El promedio de sus notas es: ",prom);
if(prom > 4.0){console.log("Messirve, lo demas es lujo");
}else{console.log("Casi casi");}*/

// S W I T C H
if(prom > 1 && prom <4){sw = 3}
else if(prom > 4 && prom <5){sw = 4;}
else if(prom > 5 && prom <6){sw = 5;}
else if(prom > 6 && prom <7){sw = 6;}
switch(sw){
    case 3:
        console.log("El promedio "+prom+" Es: Insuficiente"); break;
    case 4:
        console.log("El promedio "+prom+" Es: Suficiente");break;
    case 5:
        console.log("El promedio "+prom+" Es: Bueno");break;        
    case 6:
        console.log("El promedio "+prom+" Es: Muy bueno");break;
    default:
        console.log("Promedio no generado");break;
}
// A R R A Y
var v_arr = ["Esteban Perez", 30, 4.1, false];
/*console.log("Nombre: "+v_arr[0]);
console.log("Edad: "+v_arr[1]);
console.log("Promedio: "+v_arr[2]);
console.log("Casado: "+v_arr[3]);
*/
// CICLOS ITERATIVOS
// F O R
/*for (var i=0; i<v_arr.length; i++){
    console.log(v_arr[i]);}*/
// W H I L E
/*var wh = 0;
while (wh<v_arr.length){
    console.log("Nombre: "+v_arr[0]);
    console.log("Edad: "+v_arr[1]);
    console.log("Promedio: "+v_arr[2]);
    console.log("Casado: "+v_arr[3]);
    wh++;
}*/