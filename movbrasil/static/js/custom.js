var Validation = function () {

    return {

        //Validation
        initValidation: function () {
            $("#sky-form1").validate({
                // Rules for form validation
                rules:
                {
                    required:
                    {
                        required: true
                    },
            nome:
                    {
                        required: true,
                        nome: true
                    },
                    email:
                    {
                        required: true,
                        email: true
                    },
                    cpf:
                    {
                         required: true,
                         cpf: true
                     },
                     telefone:
                     {
                             required: true,
                             telefone:true
                     },
                     endereco:
                     {
                             required: true,
                             endereco: true
                     },
                     nro_comp:
                     {
                             required: true,
                             nro_comp: true
                     },
                     bairro:
                     {
                             required: true,
                             bairro: true
                     },
                     cidade:
                     {
                             required: true,
                             cidade: true
                     },
                     formacao:
                     {
                             required: true,
                             formacao: true
                     },
                },

                // Messages for form validation
                messages:
                {
                    required:
                    {
                       required: 'Por favor, este campo não deve ficar vazio'
                    },
           nome:
                    {
                       required: 'Por favor, insira seu nome'
                    },
                    email:
                    {
                        required: "Por favor, insira seu e-mail",
                        email: 'Por favor, insira um e-mail válido'
                    },
                    cpf:
                    {
                        required: "Por favor, insira seu cpf"
                    },
                    telefone:
                    {
                        required: "Por favor, insira seu telefone"
                    },
                    endereco:
                    {
                        required: "Por favor, insira seu endereco"
                    },
                    nro_comp:
                    {
                        required: "Por favor, insira seu número e complemento se houver."
                    },
                    bairro:
                    {
                        required: "Por favor, insira seu bairro"
                    },
                    cidade:
                    {
                        required: "Por favor, insira sua cidade "
                    },
                    formacao:
                    {
                        required: "Por favor, insira sua formacao "
                    },
                },

                // Do not change code below
                errorPlacement: function(error, element)
                {
                    error.insertAfter(element);
                }
            });
        }

    };
}();
