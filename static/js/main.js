function setLoading(target) {
  var loading = $('<h3></h3>').attr({'class': 'text-center'})
  var img = $('<img />').attr({'src': main_url+"static/img/load.svg"})
  img.appendTo(loading)
  target.html(loading)
}

// ********************* ONLOAD PAGE ******************** //
$(document).ready(function(){
  $(".data").mask("99/99/9999");
})

jQuery.validator.setDefaults({
  errorPlacement: function (error, element) {
    if(element.parents('form').hasClass('form-inline'))
      error.attr('hidden','hidden');
    element.parents('.form-group').append(error);
  },

  highlight: function(element, errorClass, validClass){
    var icon  = '<div class="input-group-append check-icon"><span class="input-group-text"><i class="fa fa-exclamation validate-icon" aria-hidden="true" style="color:#f44336"></i></span></div>';
    $(element).addClass(errorClass)
    $(element).parents('.form-group').find('label.error').remove();
  },

  success: function(label){
    label.parents('.form-group').find('.input-group').find('.check-icon').remove();
    label.parents('.form-group').find('label.error').remove();
  },

  onfocusout: function(element) {
    this.element(element);
  },
});

jQuery.validator.addMethod("validaDataLivre", function (value, element) {
  //contando chars
  if (value.length != 10) return (this.optional(element) || false);
  // verificando data
  var data = new Date();
  var anoAtual = data.getYear();
  var mesAtual = data.getMonth() + 1;
  var diaAtual = data.getDate();
  if (anoAtual < 1000){
    anoAtual+=1900;
  }

  var data = value;
  var dia = data.substr(0, 2);
  var barra1 = data.substr(2, 1);
  var mes = data.substr(3, 2);
  var barra2 = data.substr(5, 1);
  var ano = data.substr(6, 4);
  if (data.length != 10 || barra1 != "/" || barra2 != "/" || isNaN(dia) || isNaN(mes) || isNaN(ano) || dia > 31 || mes > 12) return (this.optional(element) || false);
  if ((mes == 4 || mes == 6 || mes == 9 || mes == 11) && dia == 31) return (this.optional(element) || false);
  if (mes == 2 && (dia > 29 || (dia == 29 && ano % 4 != 0))) return (this.optional(element) || false);
  if (ano < 1900) return (this.optional(element) || false);

  return (this.optional(element) || true);
}, "Informe uma data válida.");  // Mensagem padrão
