document.addEventListener("DOMContentLoaded", function() {
    //SCRIPT MOSTRAR/OCULTAR CONTRASEÑA
    document.querySelectorAll('.toggle-passwd').forEach(function(togglePassword) {
        togglePassword.addEventListener('click', function() {
            var input = this.previousElementSibling;
            if (input.type === 'password') {
                input.type = 'text';
                this.classList.remove('fa-eye');
                this.classList.add('fa-eye-slash');
            } else {
                input.type = 'password';
                this.classList.remove('fa-eye-slash');
                this.classList.add('fa-eye');
            }
        });
    });
    // NO INGRESAR CARACTERES ESPECIALES
    $.validator.addMethod("lettersOnly", function(value, element) {
        return this.optional(element) || /^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$/.test(value);
    }, "Solo se permiten letras.");

    // VALIDACION DE FORMULARIO
    $("#frm_registro_usuario").validate({
        rules:{
            primerNombre: {
                required: true,
                lettersOnly: true
            },
            segundoNombre: {
                required: true,
                lettersOnly: true
            },
            apellidoPaterno: {
                required: true,
                lettersOnly: true
            },
            apellidoMaterno: {
                required: true,
                lettersOnly: true
            },
            direccion:{
                required:true,
                minlength:5,
                maxlength:30,
            },
            telefono:{
                required:true,
                digits:true,
                maxlength:10,
            },
            email:{
                required:true,
                email:true,
            },
            usuario:{
                required:true,
                maxlength:15,
            },
            contraseña:{
                required:true,
                maxlength:10,
            },
            rol:{
                required:true,
            },
        },
        messages:{
            primerNombre: {
                required: "Campo obligatorio",
                lettersOnly: "Solo puede ingresar letras"
            },
            segundoNombre: {
                required: "Campo obligatorio",
                lettersOnly: "Solo puede ingresar letras"
            },
            apellidoPaterno: {
                required: "Campo obligatorio",
                lettersOnly: "Solo puede ingresar letras"
            },
            apellidoMaterno: {
                required: "Campo obligatorio",
                lettersOnly: "Solo puede ingresar letras"
            },
            direccion:{
                required:"Campo obligatorio",
                minlength:"Debe ingresar como mínimo 5 caracteres",
                maxlength:"Debe ingresar como máximo 30 caracteres",
            },
            telefono:{
                required:"Campo obligatorio",
                digits:"Debe ingresar solo números",
                maxlength:"Debe ingresar solo 10 dígitos",
            },
            email:{
                required:"Campo obligatorio",
                email:"Por favor, ingrese un correo electrónico válido.",
            },
            usuario:{
                required:"Campo obligatorio",
                maxlength:"Debe ingresar como máximo 15 caracteres",
            },
            contraseña:{
                required:"Campo obligatorio",
                maxlength:"Debe ingresar como máximo 10 caracteres",
            },
            rol:{
                required:"Campo obligatorio",
            },
        },
        //INGRESAR CON METODO AJAX (asincronica)
        submitHandler:function(formulario){ //funcion para peticion asincrona
            // Obtener la URL del contenedor de datos
            const urlRegistro = document.getElementById('url-container').getAttribute('data-url');
            var formData = new FormData(formulario);// Obtiene archivos multimedia y campos demás
            $.ajax({
                url:urlRegistro, //llamado a la funión de insertar
                type:'post',
                data:formData,
                contentType: false, // Necesario para enviar archivos
                processData: false, // Necesario para enviar archivos
                success:function(data){
                    if(data.estado){
                        Swal.fire({
                            title:"CONFIRMACIÓN",
                            text:data.mensaje,
                            icon:'success'
                        });
                        $(formulario)[0].reset();
                    }else{
                        Swal.fire({
                            title:"ERROR",
                            text:"Error al insertar los datos",
                            icon:'error'
                        });
                    }
                },
                error: function(xhr, status, error) {
                    alert("Error en la solicitud:", error);
                }
            });
        }
    });  
});