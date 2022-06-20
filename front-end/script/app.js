

const lanIP = `${window.location.hostname}:5000`;
const socket = io(`http://${lanIP}`);

const showTable=function(){
  
socket.on("B2F_frigo_historiek",function(jsonObject){
  
  html=[]
  for(const i of jsonObject){
     list= `
      <tr>
      <td>${i.naam} </td>     
      <td>${i.datum}</td>
      <td>${i.biernaam}</td>
      <td>${i.aantal}</td>
    </tr>`
    html+=list
    }
    document.querySelector('.js-table-frigo ').innerHTML=html
})

  socket.on("B2F_historiek", function(jsonObject){
      htmlLijst=[]
    // console.log(jsonObject)
    for(const item of jsonObject){
     lijst= `
      <tr>
      <td>${item.volgnummer} </td>     
      <td>${item.actiedatum}</td>
      <td>${item.commentaar}</td>
    </tr>`
    htmlLijst+=lijst
    }
    document.querySelector('.js-table').innerHTML=htmlLijst

    
  })
}
const bar= function(){
socket.on("B2F_bar_grafiek",function(jsonObject){
  // jsonObject= await getData()
  console.log(jsonObject  )
    lijst=[]
    let aantal_jup=[]
    let aantal_stella=[]
    let aantal_rodenbach=[]
    
    console.log(jsonObject)
    for (item of jsonObject){
      if (!lijst.includes(item.naam)){
        console.log('True')
        lijst.push(item.naam)
      }else{
        console.log('False')
      }
      if (item.naam =='kobe') {
        if (item.biernaam=='jupiler'){
          aantal_jup.push(item.aantal)
      }
    if (item.biernaam=='stella'){
          aantal_stella.push(item.aantal)
      }
      if (item.biernaam=='rodenbach'){
          aantal_rodenbach.push(item.aantal)
      }
    
    
    }
      if (item.naam=='warre'){
        if (item.biernaam=='jupiler'){
          aantal_jup.push(item.aantal)
      }
    if (item.biernaam=='stella'){
          aantal_stella.push(item.aantal)
      }
      if (item.biernaam=='rodenbach'){
          aantal_rodenbach.push(item.aantal)
      }
      }
     
    }
    console.log(lijst)  
    console.log(aantal_jup)  
     
    const CHART_COLORS = {
      red: 'rgb(255, 99, 132)',
      orange: 'rgb(255, 159, 64)',
  yellow: 'rgb(255, 205, 86)',
  green: 'rgb(75, 192, 192)',
  blue: 'rgb(54, 162, 235)',
  purple: 'rgb(153, 102, 255)',
  grey: 'rgb(201, 203, 207)'
};
const labels =lijst;
const data = {
  labels: labels,
  datasets: [
    {
      label: 'jupiler',
      data: aantal_jup,
      backgroundColor: CHART_COLORS.red,
      stack: 'Stack 0',
    },
    {
      label: 'stella',
      data: aantal_stella,
      backgroundColor: CHART_COLORS.blue,
      stack: 'Stack 1',
    },
    {
      label: 'rodenbach',
      data: aantal_rodenbach,
      backgroundColor: CHART_COLORS.green,
      stack: 'Stack 2',
    },
  ]
};
const config = {
  type: 'bar',
  data: data,
  options: {
    plugins: {
      title: {
        display: true,
        text: 'aantal drankjes per gebruiker'
      },
    },
    responsive: true,
    interaction: {
      intersect: false,
    },
    scales: {
      x: {
        stacked: true,
      },
      y: {
        stacked: true
      }
    }
  }
};

const pop = new Chart(
  document.getElementById('chart'),
  config
  )
  
})
}

const grafiek=function(){
  socket.on("B2F_temp_chart",function(jsonObject){
    let labels = [
    
  ];
  let datas=[

  ]
  // console.log(jsonObject)
 for (const item of jsonObject.waarde){
  //  console.log(item)
      labels.push(item.actiedatum)
      datas.push(item.waarde)
 }
  
  // console.log(datelist)
 

  const data = {
    labels: labels,
    datasets: [{
      label: 'Temperatuur',
      backgroundColor: 'rgb(255, 0, 0)',
      borderColor: 'rgb(255, 0, 0)',
      data: datas,
    }]
  };

  const config = {
    type: 'line',
    data: data,
    options: {
     scales: {
      y: {
        min: 15,
        max: 30,
      }
      
    }
    }
  };
  const myChart = new Chart(
    document.getElementById('myChart'),
    config
  );
  myChart()
}
)}



const listenToUI = function () {

  let btn = document.querySelector('.js-relais');
  console.log(btn)
  let status = 0
  btn.addEventListener('click', (e) => {
  status++
  console.log(status)
  if (status==2){
    status=0
  }
  socket.emit('F2B_sent', {status})

  }  
  )

};
const door=function(){
    socket.on("B2F_Frigo",function(){
    window.location.replace("192.168.168.169/frigo");
    window.location.pathname='/frigo.html'
    
  });
}
const listenToSocket = function () {
  socket.on("connected", function () {
    console.log("verbonden met socket webserver");
  });

  socket.on("B2F_send_temp", function (jsonObject) {
    console.log(jsonObject);
    waarde=jsonObject.tempwaarde
    console.log(waarde)
    htmlstring=`temperatuur waarde: ${waarde} ºC`
    document.querySelector('.js-waarde').innerHTML=htmlstring

  });
   
  socket.on("B2F_send_ip", function (jsonObject) {
    // console.log(jsonObject);
    // console.log(jsonObject.slice(2,15))
    ip=jsonObject.slice(2,15)

    document.querySelector('.js-ip').innerHTML= `<p class="js-ip">wifi: ${ip}</p>`

      });
    
  
};
const frigo=async function(){

  
  socket.on('B2F_user',function(jsonObject){
    console.log(jsonObject)
    document.querySelector('.js-user').value=jsonObject.user
  })

  
  jsonObject= await getData()
  lijst=[]
  console.log(jsonObject)
  for(item of jsonObject){
    naams=item.naam
    console.log(naams)
    lijst+=`<option value="${item.RFid}">${naams}</option>`
  }
  let Select=document.querySelector('.js-user')
  Select.innerHTML+=lijst


   const log=document.querySelectorAll('.js-plus')
   
   for (let item of log){
  
     item .addEventListener("click",function(){
       const input =item.parentNode.querySelector('input')  
       input.value++
      //  console.log(input.value)
      })

   }
    const btn=document.querySelectorAll('.js-minus')
   
   for (let item of btn){

     item.addEventListener("click",function(){
       const input =item.parentNode.querySelector('input')  
       if (input.value>0){
         input.value--

       }
      //  console.log(input.value)
      })

   }
   const submit=document.querySelector('.js-submit')
   submit.addEventListener("click",function(){
    let isError=false
     let quantity=document.querySelectorAll('.js-quantity')
     let user=document.querySelector('.js-user').value
     if (user=="user"){
      window.alert("selecteer een gebruiker")
      isError=true
     }
     let dict={}
     let lijst =[]
     for(let btn of quantity){
      if (btn.value<0){
        window.alert("geef een waarde groter of gelijk aan 0")
        isError=true
      }else{
        console.log(btn.value)
        lijst.push(btn.value)

      }
      }
      dict['bier']=(lijst)
      dict['users']=(user)
      if (!isError){
        socket.emit("F2B_update_min_fridge",{dict})
        window.location.replace("/")

      }
    //  console.log(quantity)
   })

};
const frigo_inhoud=async function(){
  
  jsonObject= await getData_inhoud()
  // console.log(jsonObject)
  lijst=[]
  // console.log(jsonObject)
  inhoud=document.querySelectorAll('.js-inhoud')
  for (let index = 0; index < inhoud.length; index++) {
    const i = inhoud[index];
    const item=jsonObject[index];
        lijst=`<p class="">${item.aantal}</p> `   
        i.innerHTML=lijst
  }
  
              
            
  //   console.log(naams)
  // console.log(inhoud)
    // lijst+=``
  // }
 


   const log=document.querySelectorAll('.js-plus')
   
   for (let item of log){
  
     item .addEventListener("click",function(){
       const input =item.parentNode.querySelector('input')  
       input.value++
      //  console.log(input.value)
      })

   }
    const btn=document.querySelectorAll('.js-minus')
   
   for (let item of btn){

     item.addEventListener("click",function(){
       const input =item.parentNode.querySelector('input')  
       if (input.value>0){
         input.value--

       }
      //  console.log(input.value)
      })

   }
   const submit=document.querySelector('.js-submit-inhoud')
   submit.addEventListener("click",function(){
    let isError=false
     let quantity=document.querySelectorAll('.js-quantity')
     
     let dict={}
     let lijst =[]
     for(let btn of quantity){
      if (btn.value<0){
        window.alert("geef een waarde groter of gelijk aan 0")
        isError=true
      }else{
        console.log(btn.value)
        lijst.push(btn.value)

      }
      }
      dict['bier']=(lijst)
      if (!isError){
        socket.emit("F2B_update_plus_fridge",{dict})
        window.location.replace("/")

      }
    //  console.log(quantity)
   })

};
async function getData(){
  let response=await fetch(`http://${lanIP}/users`)
  let data =await response.json()
  return data
}
async function getData_inhoud(){
  let response=await fetch(`http://${lanIP}/drinks`)
  // console.log(response)
  let data =await response.json()
  return data
}

 function poweroff(){
  let item = document.querySelector('.js-power');
  
  item.addEventListener('click', (e) => {
    console.log("poweroff")
  socket.emit('F2B_power')
  }  
  )
 }

document.addEventListener("DOMContentLoaded", function () {
  console.log("DOM geladen 🍺");
  if(window.location.pathname=='/'){
    
  listenToUI();
  listenToSocket();
  } 
  if(window.location.pathname=='/historiek.html'){
  showTable();
  grafiek()
  }
  if (window.location.pathname=='/user.html'){
    showTable()
    bar()
  }
  if(window.location.pathname=='/frigo.html'){

    frigo()
  }
  if (window.location.pathname=='/inhoud.html'){
    frigo_inhoud()
  }
  door()
  poweroff()
});
