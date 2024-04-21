FilePond.registerPlugin(
  FilePondPluginFileEncode,
  FilePondPluginFileValidateSize,
  FilePondPluginImageExifOrientation,
  FilePondPluginImagePreview
);
var inputMultipleElements = document.querySelectorAll(
  "input.filepond-input-multiple"
);

  FilePond.create(document.querySelector(".filepond-input-circle"), {
    labelIdle:
      'Faites glisser et déposez votre image ou <span class="filepond--label-action">Parcourir</span>',
    imagePreviewHeight: 170,
    imageCropAspectRatio: "1:1",
    imageResizeTargetWidth: 200,
    imageResizeTargetHeight: 200,
    stylePanelLayout: "compact circle",
    styleLoadIndicatorPosition: "center bottom",
    styleProgressIndicatorPosition: "right bottom",
    styleButtonRemoveItemPosition: "left bottom",
    styleButtonProcessItemPosition: "right bottom",
  }));
