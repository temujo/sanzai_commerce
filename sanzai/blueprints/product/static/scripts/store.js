// // Makes bootstrap select use native select widget of devices
// if( /Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent) ) {
//     $('.selectpicker').selectpicker('mobile');
// }

// Changes the default text of the select and deselect options
$.fn.selectpicker.Constructor.DEFAULTS.selectAllText = ' Бүгд ';
$.fn.selectpicker.Constructor.DEFAULTS.deselectAllText = ' Хоосон ';

// Changes the default text of the multiple selected text
$.fn.selectpicker.Constructor.DEFAULTS.countSelectedText = function (numSelected, numTotal) {
    return (numSelected == 1) ? '{0} сонголт' : '{0} сонголт';
  };
