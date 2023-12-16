(function () {
  // Tu código JavaScript aquí

  function createInterface() {
    /*const link = document.createElement("link");
    link.rel = "stylesheet";
    link.href="../css/chatbot.css";
    document.head.appendChild(link);*/

    // Crear la sección
    var section = document.createElement("section");
    section.className = "chat";

    // Crear el div dentro de la sección
    var div = document.createElement("div");

    // Crear la lista (ul)
    var ul = document.createElement("ul");
    ul.setAttribute("name", "msgs");

    // Crear el primer elemento de la lista (li)
    var li = document.createElement("li");
    li.textContent = "chatbot: Hola preguntame lo que necesites saber de ia";
    ul.appendChild(li);

    // Agregar la lista al div
    div.appendChild(ul);

    // Crear el formulario
    var form = document.createElement("form");

    // Crear el campo de entrada (input)
    var input = document.createElement("input");
    input.setAttribute("type", "entry");
    input.setAttribute("name", "caja");

    // Crear el botón de envío
    var submitButton = document.createElement("input");
    submitButton.setAttribute("type", "submit");

    // Agregar el campo de entrada y el botón al formulario
    form.appendChild(input);
    form.appendChild(submitButton);

    // Agregar el formulario al div
    div.appendChild(form);

    // Agregar el div a la sección
    section.appendChild(div);

    // Agregar la sección al body
    document.body.appendChild(section);
  }

  // La función que crea la interfaz
  createInterface();
})();