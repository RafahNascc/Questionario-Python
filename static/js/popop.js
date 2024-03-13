// Função para exibir o pop-up com efeito de fade-in
function fadeInPopup(popupSelector) {
    $(popupSelector).css({ opacity: 0, display: "block" });
    setTimeout(function () {
        $(popupSelector).animate({ opacity: 1 }, 400);
    }, 100); // Aguarde 100 milissegundos antes de iniciar o efeito
}


// Função para abrir o pop-up
function checklist() {
    document.getElementById("pop-up").style.display = "block";
}

// Função para fechar o pop-up
function fecharPopUp() {
    document.getElementById("pop-up").style.display = "none";
}

// Função para enviar os dados do formulário
function enviarDados() {
    var perguntas = {}; // Seus dados do formulário aqui

    var radios = document.querySelectorAll('input[name^="p"]');
    radios.forEach(function (radio) {
        if (radio.checked) {
            perguntas[radio.name] = radio.value;
        }
    });




    // Adicione o valor do radio button ao objeto de dados
    perguntas['status'] = $('input[name="status"]:checked').val();
    perguntas['status'] = perguntas['status'].toString();

    perguntas['identificação'] = $('input[name="identificação"]:checked').val();
    perguntas['identificação'] = perguntas['identificação'].toString();

    perguntas['aspecto'] = $('input[name="aspecto"]:checked').val();
    perguntas['aspecto'] = perguntas['aspecto'].toString();

    perguntas['memoria'] = $('input[name="memoria"]:checked').val();
    perguntas['memoria'] = perguntas['memoria'].toString();

    perguntas['montagem_direcao'] = $('input[name="montagem_direcao"]:checked').val();
    perguntas['montagem_direcao'] = perguntas['memormontagem_direcaoia'].toString();

    perguntas['identificação_direcao'] = $('input[name="identificação_direcao"]:checked').val();
    perguntas['identificação_direcao'] = perguntas['identificação_direcao'].toString();

    perguntas['aspecto_direcao'] = $('input[name="aspecto_direcao"]:checked').val();
    perguntas['aspecto_direcao'] = perguntas['aspecto_direcao'].toString();

    perguntas['montagem_tracao'] = $('input[name="montagem_tracao"]:checked').val();
    perguntas['montagem_tracao'] = perguntas['montagem_tracao'].toString();

    perguntas['freio_tracao'] = $('input[name="freio_tracao"]:checked').val();
    perguntas['freio_tracao'] = perguntas['freio_tracao'].toString();

    perguntas['identificação_tracao'] = $('input[name="identificação_tracao"]:checked').val();
    perguntas['identificação_tracao'] = perguntas['identificação_tracao'].toString();
    
    perguntas['aspecto_tracao'] = $('input[name="aspecto_tracao"]:checked').val();
    perguntas['aspecto_tracao'] = perguntas['aspecto_tracao'].toString();

    perguntas['montagem_sensores'] = $('input[name="montagem_sensores"]:checked').val();
    perguntas['montagem_sensores'] = perguntas['montagem_sensores'].toString();

    perguntas['identificação_sensores'] = $('input[name="identificação_sensores"]:checked').val();
    perguntas['identificação_sensores'] = perguntas['identificação_sensores'].toString();

    perguntas['aspecto_sensores'] = $('input[name="aspecto_sensores"]:checked').val();
    perguntas['aspecto_sensores'] = perguntas['aspecto_sensores'].toString();

    perguntas['montagem_engate'] = $('input[name="montagem_engate"]:checked').val();
    perguntas['montagem_engate'] = perguntas['montagem_engate'].toString();

    perguntas['hidráulico_engate'] = $('input[name="hidráulico_engate"]:checked').val();
    perguntas['hidráulico_engate'] = perguntas['hidráulico_engate'].toString();

    perguntas['identificação_engate'] = $('input[name="identificação_engate"]:checked').val();
    perguntas['identificação_engate'] = perguntas['identificação_engate'].toString();

    perguntas['montagem_baterias'] = $('input[name="montagem_baterias"]:checked').val();
    perguntas['montagem_baterias'] = perguntas['montagem_baterias'].toString();

    perguntas['identificação_baterias'] = $('input[name="identificação_baterias"]:checked').val();
    perguntas['identificação_baterias'] = perguntas['identificação_baterias'].toString();

    perguntas['aspecto_baterias'] = $('input[name="aspecto_baterias"]:checked').val();
    perguntas['aspecto_baterias'] = perguntas['aspecto_baterias'].toString();

    perguntas['montagem_botoeira'] = $('input[name="montagem_botoeira"]:checked').val();
    perguntas['montagem_botoeira'] = perguntas['montagem_botoeira'].toString();

    perguntas['identificação_botoeira'] = $('input[name="identificação_botoeira"]:checked').val();
    perguntas['identificação_botoeira'] = perguntas['identificação_botoeira'].toString();

    perguntas['aspecto_botoeira'] = $('input[name="aspecto_botoeira"]:checked').val();
    perguntas['aspecto_botoeira'] = perguntas['aspecto_botoeira'].toString();

    perguntas['montagem_tampas'] = $('input[name="montagem_tampas"]:checked').val();
    perguntas['montagem_tampas'] = perguntas['montagem_tampas'].toString();

    perguntas['raspadores_tampas'] = $('input[name="raspadores_tampas"]:checked').val();
    perguntas['raspadores_tampas'] = perguntas['raspadores_tampas'].toString();

    perguntas['aspecto_tampas'] = $('input[name="aspecto_tampas"]:checked').val();
    perguntas['aspecto_tampas'] = perguntas['aspecto_tampas'].toString();

    perguntas['teste_tampas'] = $('input[name="teste_tampas"]:checked').val();
    perguntas['teste_tampas'] = perguntas['teste_tampas'].toString();

    perguntas['torqueamento_tampas'] = $('input[name="torqueamento_tampas"]:checked').val();
    perguntas['torqueamento_tampas'] = perguntas['torqueamento_tampas'].toString();

    perguntas['pintura_equipaamento'] = $('input[name="pintura_equipaamento"]:checked').val();
    perguntas['pintura_equipaamento'] = perguntas['pintura_equipaamento'].toString();

    perguntas['adesivos_equipamento'] = $('input[name="adesivos_equipamento"]:checked').val();
    perguntas['adesivos_equipamento'] = perguntas['adesivos_equipamento'].toString();

    perguntas['joystick_equipamento'] = $('input[name="joystick_equipamento"]:checked').val();
    perguntas['joystick_equipamento'] = perguntas['joystick_equipamento'].toString();


    
    // Crie um objeto FormData com os dados
    var formData = new FormData();
    for (var key in perguntas){
        formData.append(key, perguntas[key]);
    }

    // Envie os dados para o servidor
    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(perguntas),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        fecharPopUp(); // Feche o pop-up após o envio
    })
    .catch(error => {
        console.error(error);
    });


}


$(document).ready(function() {
    $('#myForm').submit(function(event) {
        event.preventDefault(); // Impede o envio normal do formulário
        
        // Coleta os dados do formulário
        var responsavel = $('input[name="responsavel"]').val();
        var data = $('input[name="data"]').val();
        var serial = $('input[name="serial"]').val();
        var comentario1 = $('input[name="comentario1"]').val();
        var comentario2 = $('input[name="comentario2"]').val();
        var comentario3 = $('input[name="comentario3"]').val();
        var comentario4 = $('input[name="comentario4"]').val();
        var comentario5 = $('input[name="comentario5"]').val();
        var comentario6 = $('input[name="comentario6"]').val();
        var comentario7 = $('input[name="comentario7"]').val();
        var comentario8 = $('input[name="comentario8"]').val();
        var comentario9 = $('input[name="comentario9"]').val();
        var comentario10 = $('input[name="comentario10"]').val();
        var comentario11 = $('input[name="comentario11"]').val();
        var comentario12 = $('input[name="comentario12"]').val();
        var comentario13 = $('input[name="comentario13"]').val();
        var comentario14 = $('input[name="comentario14"]').val();
        var comentario15 = $('input[name="comentario15"]').val();
        var comentario16 = $('input[name="comentario16"]').val();
        var comentario17 = $('input[name="comentario17"]').val();
        var comentario18 = $('input[name="comentario18"]').val();
        var comentario19 = $('input[name="comentario19"]').val();
        var comentario20 = $('input[name="comentario20"]').val();
        var comentario21 = $('input[name="comentario21"]').val();
        var comentario22 = $('input[name="comentario22"]').val();
        var comentario23 = $('input[name="comentario23"]').val();
        var comentario24 = $('input[name="comentario24"]').val();
        var comentario25 = $('input[name="comentario25"]').val();
        var comentario26 = $('input[name="comentario26"]').val();
        var comentario27 = $('input[name="comentario27"]').val();
        var comentario28 = $('input[name="comentario28"]').val();
        var comentario29 = $('input[name="comentario29"]').val();
        var comentario30 = $('input[name="comentario30"]').val();
        var comentario31 = $('input[name="comentario31"]').val();
        var comentario32 = $('input[name="comentario32"]').val();


        // Cria um objeto com os dados
        var formData = {
            responsavel: responsavel,
            data: data,
            serial: serial,
            comentario1: comentario1,
            comentario2: comentario2,
            comentario3: comentario3,
            comentario4: comentario4,
            comentario5: comentario5,
            comentario6: comentario6,
            comentario7: comentario7,
            comentario8: comentario8,
            comentario9: comentario9,
            comentario10: comentario10,
            comentario11: comentario11,
            comentario12: comentario12,
            comentario13: comentario13,
            comentario14: comentario14,
            comentario15: comentario15,
            comentario16: comentario16,
            comentario17: comentario17,
            comentario18: comentario18,
            comentario19: comentario19,
            comentario20: comentario20,
            comentario21: comentario21,
            comentario22: comentario22,
            comentario23: comentario23,
            comentario24: comentario24,
            comentario25: comentario25,
            comentario26: comentario26,
            comentario27: comentario27,
            comentario28: comentario28,
            comentario29: comentario29,
            comentario30: comentario30,
            comentario31: comentario31,
            comentario32: comentario32,


            status: $('input[name="status"]:checked').val(),
            identificação: $('input[name="identificação"]:checked').val(),
            aspecto: $('input[name="aspecto"]:checked').val(),
            memoria: $('input[name="memoria"]:checked').val(),

            montagem_direcao: $('input[name="montagem_direcao"]:checked').val(),
            identificação_direcao: $('input[name="identificação_direcao"]:checked').val(),
            aspecto_direcao: $('input[name="aspecto_direcao"]:checked').val(),

            montagem_tracao: $('input[name="montagem_tracao"]:checked').val(),
            freio_tracao: $('input[name="freio_tracao"]:checked').val(),
            identificação_tracao: $('input[name="identificação_tracao"]:checked').val(),
            aspecto_tracao: $('input[name="aspecto_tracao"]:checked').val(),

            montagem_sensores: $('input[name="montagem_sensores"]:checked').val(),
            identificação_sensores: $('input[name="identificação_sensores"]:checked').val(),
            aspecto_sensores: $('input[name="aspecto_sensores"]:checked').val(),

            montagem_engate: $('input[name="montagem_engate"]:checked').val(),
            hidráulico_engate: $('input[name="hidráulico_engate"]:checked').val(),
            identificação_engate: $('input[name="identificação_engate"]:checked').val(),
            aspecto_engate: $('input[name="aspecto_engate"]:checked').val(),

            montagem_baterias: $('input[name="montagem_baterias"]:checked').val(),
            identificação_baterias: $('input[name="identificação_baterias"]:checked').val(),
            aspecto_baterias: $('input[name="aspecto_baterias"]:checked').val(),

            montagem_botoeira: $('input[name="montagem_botoeira"]:checked').val(),
            identificação_botoeira: $('input[name="identificação_botoeira"]:checked').val(),
            aspecto_botoeira: $('input[name="aspecto_botoeira"]:checked').val(),

            montagem_tampas:$('input[name="montagem_tampas"]:checked').val(),
            raspadores_tampas: $('input[name="raspadores_tampas"]:checked').val(),
            aspecto_tampas: $('input[name="aspecto_tampas"]:checked').val(),
            teste_tampas: $('input[name="teste_tampas"]:checked').val(),
            torqueamento_tampas: $('input[name="torqueamento_tampas"]:checked').val(),

            pintura_equipaamento: $('input[name="pintura_equipaamento"]:checked').val(),
            adesivos_equipamento: $('input[name="adesivos_equipamento"]:checked').val(),
            joystick_equipamento: $('input[name="joystick_equipamento"]:checked').val()

        };

        // Envia os dados para o servidor usando AJAX
        $.ajax({
            type: 'POST',
            url: '/submit',
            data: formData,
            success: function(response) {
                // Manipula a resposta do servidor aqui, se necessário
                console.log(response);
                // Exibe um pop-up de sucesso personalizado com um botão "X"
                var successPopup = '<div class="custom-popup success-popup">' +
                                  '<span class="close-button">X</span>' +
                                  'Sucesso!</div>';
                $("body").append(successPopup);
                fecharPopUp();
            
                // Adicione o código para fechar o pop-up ao clicar no botão "X"
                $(document).on("click", ".close-button", function() {
                    $(this).parent().fadeOut("slow", function() {
                        $(this).remove(); // Remove o pop-up ao completar o fade-out
                    });
                });
                // Exibe o pop-up com fade-in
                fadeInPopup(".custom-popup.success-popup");
            },
            error: function(error) {
                // Manipula erros aqui, se necessário
                console.error(error);
                // Exibe um pop-up de erro personalizado com um botão "X"
                var errorPopup = '<div class="custom-popup error-popup">' +
                                '<span class="close-button">X</span>' +
                                'Erro!</div>';
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
        });
    });
});
