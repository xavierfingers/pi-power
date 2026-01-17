package main
import (
 "net/http"
 "fmt"
 _ "modernc.org/sqlite"
 "database/sql"
 "sync"
)
var (
 messageMutex sync.Mutex
 scanned string
)
func main() {
 pool := []string{
  "messages.db",
  "users.db",
 }
 cluster2, _ := sql.Open("sqlite", pool[0])
 cluster3, _ := sql.Open("sqlite", pool[1])
 cluster3.Exec("CREATE TABLE users(name varchar(255))")
 cluster2.Exec("CREATE TABLE message(cntent varchar(255), name varchar(255))")
 mux := http.NewServeMux()
 mux.HandleFunc("/user/register/{name}", func(w http.ResponseWriter, r *http.Request) {
   name := r.PathValue("name")
   messageMutex.Lock()
   cluster3.Exec("INSERT INTO users(name) VALUES (?)", name)
   messageMutex.Unlock()
   fmt.Fprintf(w, "Created user %s", name)
  })
  mux.HandleFunc("/send/{name}/{message}", func(w http.ResponseWriter, r *http.Request) {
    message := r.PathValue("message")
    name := r.PathValue("name")
    cluster2.Exec("INSERT INTO message(cntent, name) VALUES (?, ?)", message, name)
   })
   mux.HandleFunc("/messages/list", func(w http.ResponseWriter, r *http.Request) {
    x, _ := cluster2.Query("SELECT content FROM message")
    for x.Next() {
     x.Scan(&scanned)
   fmt.Fprintf(w, "Content: %s", scanned)
   }
  })
  http.ListenAndServe(":8080", mux)
 }        
