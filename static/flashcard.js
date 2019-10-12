dlists = {}
var currDlist;
var currIndex;
var onTerm = false;
$(document).ready(function () {
  // Grab all sections
  $('.flashcard-content h2').each(function () {
    let section = $(this)
    let sectionTitle = section.text();
    $("#flashcards").append(
      `<li class="list-group-item-action"><button class="btn btn-link pl-0" onclick="load_flashcard('${sectionTitle}')">${sectionTitle}</btn></li>`
    )

    // Grab all the terms and definitions
    let dl = section.next()
    console.log(section);
    let terms = $(dl).children("dt");
    let defs = $(dl).children("dd");

    dlists[sectionTitle] = {
      'terms': terms,
      'defs': defs,
      'length': terms.length,
    };

  });
  $(".flashcard-content").empty();
});

function load_flashcard(sectionTitle) {
  $(".flashcard").removeClass('d-none')
  $(".title").html(sectionTitle)
  $(".flashcard-content").empty();

  // Get and shuffle the definition list
  currDlist = dlists[sectionTitle]
  for (let i = currDlist['length'] - 1; i > 0; i--) {
    let j = Math.floor(Math.random() * (i + 1));

    let temp = currDlist['terms'][i];
    currDlist['terms'][i] = currDlist['terms'][j];
    currDlist['terms'][j] = temp;

    temp = currDlist['defs'][i];
    currDlist['defs'][i] = currDlist['defs'][j];
    currDlist['defs'][j] = temp;
  };

  currIndex = -1;
  next_term();
};

function next_term() {
  if (currIndex + 1 >= currDlist['length']) {
    return;
  }

  currTerm = currDlist['terms'][currIndex + 1];
  $(".flashcard-content").html(currTerm);;

  currIndex++;
  $(".flashcard-counter").html(`${currIndex + 1}/${currDlist['length']}`)
  onTerm = true;
  MathJax.typeset();
};

function prev_term() {
  if (currIndex < 0) {
    return;
  }

  currTerm = currDlist['terms'][currIndex];
  $(".flashcard-content").html(currTerm);

  onTerm = true;
  MathJax.typeset();
};

function next_definition() {
  currDef = currDlist['defs'][currIndex];
  $(".flashcard-content").html(currDef);

  onTerm = false;
  MathJax.typeset();
}

function prev_definition() {
  if (currIndex - 1 < 0) {
    return;
  }

  currTerm = currDlist['terms'][currIndex - 1];
  $(".flashcard-content").html(currDef);

  currIndex--;
  $(".flashcard-counter").html(`${currIndex + 1}/${currDlist['length']}`);
  onTerm = false;
  MathJax.typeset();
};

$(".flashcard-next").click(function () {
  if (onTerm) {
    next_definition();
    onTerm = false;
  } else {
    next_term();
    onTerm = true;
  }
})

$(".flashcard-prev").click(function () {
  if (onTerm) {
    prev_definition();
  } else {
    prev_term();
  }
})