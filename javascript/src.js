//Number //числа
//String //строки
//Boolean //истина или ложь
//undefined  // неопределенное
//object //объект
//NaN    //пустота

//let user = new Object(); //конструктор объекта
//user = {                       // задаем объекту его параметры
//    name: "John Doe",
//    age: 30,
//    surname: "Doe",
//    hobby: "Play tennis"
//}
//
//alert(user.name); // vivod v oshibky
//alert(user.age);
//
//let age = 19;
//let name = "john";
//let check = false;
//
//console.log(user.name); //vivod v konsol
//
//var age2 = 20;
//function returning(){
//    let number = 19;
//    alert(number);
//}
//returning();
//alert(number);
//
//const g = 9.8; //konstanta
//
//alert (age==age2) //operator sravnenie, prover
//alert (age===age2) //proverka na identichnost vsego obekta
//
//let sum = age + age2;
//
//alert(name + "." + age2.toString()); //obernut v stroku
//
//alert(Number(name) + age); //obernut v chislo

//
//let userAge = +prompt("Enter your age: "); //input  string
//alert(typeof(userAge)); //pozvolayet uznat tip  + //poluchaem number
//
//let check = confirm("Are you sure you want to check your age?"); //pozvolaet poluchit true ili folse
//alert(check);


///////////////////////////////////////////////////////////////////////////////////////////
let a = 5
//while(a!=0) {
//    alert("wmth")
//    a--;
//}
//
//do {
//    alert("smth");
//    a--;
//}while(a!=0)

//for(let i=0; i<a; i++){
//    alert("swth");
//    alert(a);
//    alert(i);
//    if (i==3){
////        break;
//        continue;
//    }

//}
//break;

//let a = +prompt("Enetr your number");
//while(a!=0){
//    alert("#");
//    a--;
//}


//let a = +prompt("Enetr your number");
//while (a > 0){
//    alert(a);
//    a--;
//}

//let a = +prompt("Enetr your number");
//let b = +prompt("Enetr your power");
//let c = a;
//while(b>1){
//    b--;
//    a=a*c;
//}
//alert(a);

//let a = +prompt("Enter your number");
//let b = +prompt("Enter your number");
//let i = 1;
//let arr = [];
//function pickMin(a, b){
//    if (a > b){
//        return b;
//        }
//        else return a;
//        }
//function pickMax(a, b){
//    if (a > b){
//        return a; }
//    else return b; }
//
//while(i>pickMin(a, b)){
//    if(pickMax(a, b)%i==0 && pickMin(a, b)%i==0){
//    arr.push(i);
//    }
//    i++;
//    alert(i); }
//    alert(arr);
//
//while(a){
//    if (a>b){
//
//
//    }
//}


//let number = +prompt("Enter your number");
//let result = 1;
//while(number != 0){
//    result *=number;
//    number--;
//}
//alert(result);
//
//function factorial(number){
//    return number?number*factorial(number-1):1;
//}

//let result;
//
//do{
//    result = +prompt(entercorrect result);
//}while(result!= 2+2*2)

//let a = 50;
//let result = 1000;
//let cnt = 0;
//do{
//    result = result/2;
//    cnt++;
//}while(result>50);
//alert(cnt);


//let number = +prompt("Rneter your number ");
//for(let i = 1; i<= 100; i++){
//    if(number%i==0){
//        alert(i);
//    }
//}

let a = +prompt("Rneter your number ");
let b = +prompt("Rneter your number ");
let arr = [];

let substraction = b - a;
for(let i = 0; i<substraction; i++){
    arr.push(a);
    a++;
}

for(let i = 1; i <= Math.abs(a-b); i++)
    if(i%4==0){
        alert(arr[i]);
    }
}