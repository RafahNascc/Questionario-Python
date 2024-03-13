// Função para exibir o pop-up com efeito de fade-in
function fadeInPopup(popupSelector) {
    $(popupSelector).css({ opacity: 0, display: "block" });
    setTimeout(function () {
        $(popupSelector).animate({ opacity: 1 }, 400);
    }, 100); // Aguarde 100 milissegundos antes de iniciar o efeito
}

function checkLogin() {
    // Obter os valores de entrada do usuário
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Criar um objeto de solicitação XMLHttpRequest
    var xhr = new XMLHttpRequest();

    // Configurar a solicitação para enviar um POST request para a rota '/verificar_login'
    xhr.open("POST", "/verificar_login", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

    // Configurar a função de retorno de chamada para a resposta do servidor
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.success) {
                // Exibe um pop-up de sucesso personalizado com um botão "X"
                var successPopup = '<div class="custom-popup success-popup">' +
                                  '<span class="close-button">X</span>' +
                                  'Bem-sucedido!</div>';
                $("body").append(successPopup);
            
                // Adicione o código para fechar o pop-up ao clicar no botão "X" e, em seguida, redirecionar
                $(document).on("click", ".close-button", function() {
                    $(this).parent().fadeOut("slow", function() {
                        $(this).remove(); // Remove o pop-up ao completar o fade-out
                        window.location.href = "/home"; // Redirecionar para a página de login
                    });
                });
                // Exibe o pop-up com fade-in
                fadeInPopup(".custom-popup.success-popup");
            } else {
                // Exibe um pop-up de erro personalizado com um botão "X"
                var errorPopup = '<div class="custom-popup error-popup">' +
                                '<span class="close-button">X</span>' +
                                'Erro! </div>';
                $("body").append(errorPopup);
            
                // Adicione o código para fechar o pop-up ao clicar no botão "X"
                $(document).on("click", ".close-button", function() {
                    $(this).parent().fadeOut("slow", function() {
                        $(this).remove(); // Remove o pop-up ao completar o fade-out
                    });
                });

                // Exibe o pop-up com fade-in
                fadeInPopup(".custom-popup.error-popup");
            }            
        }
    };

    // Enviar os dados de login como JSON para o servidor
    var data = JSON.stringify({ "username": username, "password": password });
    xhr.send(data);
}