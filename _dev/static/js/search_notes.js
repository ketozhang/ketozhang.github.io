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
        url_as_nav = page.url.slice(1, -1).replace(/\//g, ' > ');
        result_box.append(
            `<a id="search_result_${id}" class="list-group-item list-group-item-action" href="${page.url}"><strong>${page.title}</strong> <small class="text-muted">${url_as_nav}</small></a>`
        )
        if (page.content !== null) {
            content = $(page.content).text()
            var preview = content.split(" ", 20).join(" ")
            $(`#search_result_${id}`).append(`<div class="text-muted">${preview}</div>`)
        }

    })
}