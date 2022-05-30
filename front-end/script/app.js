const lanIP = `${window.location.hostname}:5000`;
const socket = io(`http://${lanIP}`);



const listenToUI = function () {
  const temperatuur = document.querySelector(".js-waarde");
  waarde=temperatuur.temp
      socket.emit("F2B_sent", {'temp': waarde });

};

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
        // socket.emit("F2B_sent", {'temp': waarde });

    // for (const temp of jsonObject) {
    //   const room = document.querySelector(`.js-room[data-idlamp="${lamp.id}"]`);
    //   if (room) {
    //     const knop = room.querySelector(".js-power-btn");
    //     knop.dataset.statuslamp = lamp.status;
    //     clearClassList(room);
    //     if (lamp.status == 1) {
    //       room.classList.add("c-room--on");
    //     }
    //   }
    // }
  });

//   socket.on("B2F_verandering_lamp", function (jsonObject) {
//     console.log("Er is een status van een lamp veranderd");
//     console.log(jsonObject.lamp.id);
//     console.log(jsonObject.lamp.status);

//     const room = document.querySelector(`.js-room[data-idlamp="${jsonObject.lamp.id}"]`);
//     if (room) {
//       const knop = room.querySelector(".js-power-btn"); //spreek de room, als start. Zodat je enkel knop krijgt die in de room staat
//       knop.dataset.statuslamp = jsonObject.lamp.status;

//       clearClassList(room);
//       if (jsonObject.lamp.status == 1) {
//         room.classList.add("c-room--on");
//       }
//     }
//   });
//   socket.on("B2F_verandering_lamp_from_HRDWR", function (jsonObject) {
//     console.log(jsonObject)
//   }) 

};

document.addEventListener("DOMContentLoaded", function () {
  console.info("DOM geladen 🍺");
  listenToUI();
  listenToSocket();
});
