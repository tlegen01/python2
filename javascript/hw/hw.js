//1
//let userAge = prompt("Enter your name: ");
//alert("Привет: " + userAge);
//2
//let userAge = +prompt("Enter your age: ");
//const age = 2022;
//alert(age - userAge);
//3
//let userAge = +prompt("Vvedite storonu kvadrata: ");
//alert(userAge * 2);
//4.1
//let userAge = +prompt("Vvedite radius: ");
//const pia = 3.14;
//alert(pia * userAge ** 2);
//4.2
//let userAge = +prompt("Vvedite radius: ");
//const pia = 3.14;
//let stepen = Math.pow(userAge, 2)
//alert(pia * stepen);
//5
//let userR = +prompt("Vvedite rastoyanie: ");
//let userV = +prompt("Vvedite vremya: ");
//alert(userR/userV + " k/ch");
//6
//let userD = +prompt("Vvedite summu v Dolarah ");
//const euro = 0.9970;
//alert(userD * euro + " E");
//7
//let fleshG = +prompt("obem flash v gigabaitah: ");
//let fleshM = fleshG * 1024;
//const obemM = 820;
//alert(Math.floor(fleshM/obemM));
//8
//let koshelek = +prompt("Vvedite summu: ");
//let cena = +prompt("Vvedite cenu: ");
//alert(Math.floor(koshelek/cena) + " sht");
//alert(koshelek%cena + " ostatok");
//9
let nummber = +prompt("Vvedite chislo: ");
let number1 = nummber % 10;
let number2 = Math.floor((nummber % 100) / 10);

let number3 = Math.floor((nummber % 1000) / 100);
alert(number1 + "" + number2 + "" + number3);