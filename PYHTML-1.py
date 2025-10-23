import pyhtml as h
t=h.html(
    h.head(
        h.title("Test Page")
    ),
    h.body(
        h.h1("This is a test page"),
        h.div("This is a test div"),
        h.div(h.h2("This is a test page"),h.p("This is a test page"))
    )
)
print(t.render())