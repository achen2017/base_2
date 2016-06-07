Rails.application.routes.draw do
  get('/', { :controller => 'query', :action => 'index' })
  get('/start_query', { :controller => 'query', :action => 'create_row'})


  get "/query/:id", :controller => "query", :action => "show"
  get "/delete_query/:id", :controller => "query", :action => "destroy"

  get('/delete_newest', { :controller => 'query', :action => 'destroy_newest' })
  get('/delete/:id', { :controller => 'query', :action => 'destroy_selected' })

  get('/about', { :controller => 'query', :action => 'about' })
end
