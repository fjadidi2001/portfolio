package main

import (
	"html/template"
	"net/http"
	"os/exec"
)

// Handler Functions
func serveStaticFile(w http.ResponseWriter, r *http.Request) {
	http.ServeFile(w, r, r.URL.Path[1:])
}

/*serveStaticFile: This function is a simple static file server that allows us to serve static files
(like CSS, images, etc.) from the static directory. It uses http.ServeFile to handle the file serving.

*/
func indexHandler(w http.ResponseWriter, r *http.Request) {
	tmpl, err := template.ParseFiles("templates/index.html")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	tmpl.Execute(w, nil)
}
func buildHandler(w http.ResponseWriter, r *http.Request) {
	cmd := exec.Command("./build.sh")
	output, err := cmd.CombinedOutput()
	if err != nil {
		http.Error(w, "Failed to execute the build script.", http.StatusInternalServerError)
		return
	}
	w.Header().Set("Content-Type", "text/plain")
	w.Write(output)
}

func educationHandler(w http.ResponseWriter, r *http.Request) {
	tmpl, err := template.ParseFiles("templates/education.html")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	tmpl.Execute(w, nil)
}

/* indexHandler: This function handles the root URL / of our website.
It reads the index.html file from the templates folder, parses it using the template package, and then executes the template by passing nil as data.
*/
func main() {
	http.HandleFunc("/static/", serveStaticFile)
	http.HandleFunc("/", indexHandler)
	http.HandleFunc("/build", buildHandler)
	http.HandleFunc("/education", educationHandler)

	port := "8080"
	println("Server listening on port", port)
	err := http.ListenAndServe(":"+port, nil)
	if err != nil {
		panic(err)
	}
}
