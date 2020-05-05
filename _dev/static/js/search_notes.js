const fuse_options = {
    keys: ["title"],
    minMatchCharLength: 3,
    threshold: 0.3,
    useExtendedSearch: true
}
const fuse = new Fuse(pages, fuse_options)
$("#dummy_search_notes").mousedown(function () {
    $("#search_modal").modal('show')
}
)

$('#search_modal').on('shown.bs.modal', function () {
    $("#search_notes").trigger('focus')
})

function search_notes() {
    var query = $("#search_notes").val();
    var results = fuse.search(query)
    var result_box = $("#search_results")

    result_box.empty()
    results.forEach(function (result, id) {
        var page = result.item
        result_box.append(`<li> <a href="${page.url}">${page.title}</a> </li>`)
    })
}