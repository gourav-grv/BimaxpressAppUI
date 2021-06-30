// window.onload = Grid;
console.log('javscript is working js.js');
var homeMiddleLineForListAndGrid = document.getElementById(
  "homeMiddleLineForListAndGrid"
);

function Drafts() {
  homeMiddleLineForListAndGrid.style.backgroundColor = "rgb(167, 47, 67)";
}
function Unprocessed() {
  homeMiddleLineForListAndGrid.style.backgroundColor = "skyblue";
}
function NMI() {
  homeMiddleLineForListAndGrid.style.backgroundColor = "darkblue";
}
function Approved() {
  homeMiddleLineForListAndGrid.style.backgroundColor = "lightgreen";
}
function Rejected() {
  homeMiddleLineForListAndGrid.style.backgroundColor = "red";
}
function Enhance_Discharge() {
  homeMiddleLineForListAndGrid.style.backgroundColor = "orange";
}
function Discharge_Approved() {
  homeMiddleLineForListAndGrid.style.backgroundColor = "rgb(9, 163, 9)";
}
function All_Processed() {
  homeMiddleLineForListAndGrid.style.backgroundColor = "black";
}
var homeBottomCards = document.getElementById("homeBottomCards");
var grid = document.getElementById("grid");



function Grid() {
  grid.classList = "glyphicon glyphicon-th-large text-black";
  list.classList = "glyphicon glyphicon-th-list text-white GridLIst";

  homeBottomCards.innerHTML = `
  
`;
}

var list = document.getElementById("list");
function List() {
  list.classList = "glyphicon glyphicon-th-list text-black GridLIst";
  grid.classList = "glyphicon glyphicon-th-large text-white";
  homeBottomCards.innerHTML = `
  
  `;
}

var sidenav = document.getElementById("sidenav");

function navHover() {
  sidenav.innerHTML = `<div><i class="glyphicon glyphicon-home activeIcon"></i><b>Home</b></div>
    <div><i class="glyphicon glyphicon-plus"></i><b>New-Claim</b></div>
    <div><i class="glyphicon glyphicon-envelope"></i><b>Inbox</b></div>
    <div><i class="glyphicon glyphicon-user"></i><b>Profile</b></div>
    <div><i class="glyphicon glyphicon-cog"></i><b>Settings</b></div>`;
}
function mainHover() {
  sidenav.innerHTML = `        <div><i class="glyphicon glyphicon-home activeIcon"></i></div>
    <div><i class="glyphicon glyphicon-plus"></i></div>
    <div><i class="glyphicon glyphicon-envelope"></i></div>
    <div><i class="glyphicon glyphicon-user"></i></div>
    <div><i class="glyphicon glyphicon-cog"></i></div>`;
}
