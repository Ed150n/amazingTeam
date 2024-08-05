document.addEventListener("DOMContentLoaded", function() {
    //SCRIPT MOSTRAR/OCULTAR CONTRASEÑA
    document.querySelectorAll('.toggle-password').forEach(function(togglePassword) {
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
    //VALIDAR MODAL
    $("#frm_inicio_sesion").validate({
        rules:{
            username:{
                required:true,
            },
            password:{
                required:true,
            }
        },
        messages:{
            username:{
                required:"Campo obligatorio",
            },
            password:{
                required:"Campo obligatorio",
            }
        },
        // 
    });
});
