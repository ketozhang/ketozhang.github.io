directives = [".Example", ".Proof"].join(", ")

$(directives).click(function () {
    let content = $(this).children();
    $(content).slideToggle(300);
});