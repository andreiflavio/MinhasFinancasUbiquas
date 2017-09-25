$(document).ready(function(){
    
    montaComboBox("#cbbMes", ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]);
    
    montaComboBox("#cbbAno", ["2017","2018","2019","2020","2021","2022","2023"]);

    now = new Date;    
    var mesAtual = now.getMonth();
    cbbMes.options[mesAtual].selected = true;
    
    var anoAtual = now.getFullYear();            
    for (i = 0; i < cbbAno.options.length; i++)
    {
        if (cbbAno.options[i].value = anoAtual)
        {
            cbbAno.options[i].selected = true;
            break;
        }
    }
});

var montaComboBox = function(nomeCbb, conteudoCbb){
    var comboBox = $(nomeCbb);
    for (var i = 0; i< conteudoCbb.length; i++)
    {
        comboBox.append($('<option>', { value:i+1, text:conteudoCbb[i]}));
    }
};