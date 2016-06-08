class QueryController < ApplicationController
  def index
    @queries = Query.all
    # @data = Datum.all
    @run_spin = TRUE


    if Datum.maximum(:id).class == NilClass
      @data = Datum.all
      @query = FALSE
    else
      @data = Datum.where(:query_id => Datum.maximum(:query_id))
      @query = Query.find(Datum.maximum(:query_id))
    end

    # @data = Datum.where(:id => Datum.maximum(:id))
    # @latest_id = Query.order(:created_at desc, :limit => 1)
    # @latest_id = Query.find(:order => "created_at", :limit => 1)


    # You need to recreate the data array
    @modules = []
    @data.each do |line|

        big_module = line['module'].split(":")[0]
        if @modules.include?(big_module) != TRUE
          @modules << big_module
        end
    end


  end



  def show
    @queries = Query.all
    @query = Query.find(params[:id])
    @data = Datum.where(:query_id => params[:id])

    @modules = []
    @data.each do |line|

      big_module = line['module'].split(":")[0]
      if @modules.include?(big_module) != TRUE
        @modules << big_module
      end

    end
  end



  def new_form   ### I might not even need this
  end

  def about
    @queries = Query.all
    render 'about'   ### I might not even need this
  end

  def create_row

    @run_spin = TRUE
    @query = Query.new
    @query.query = params[:query]
    @query.save

    if Datum.maximum(:id).class == NilClass
      @latest_id = '0'
    else
      @latest_id = Datum.maximum(:id).to_s
    end

    a = Query.maximum(:id).to_s
    # system('python python_old/web_scraper_5.py ' + params[:query] + " " + @latest_id)


    if params[:query].include?(" ")
      mouse = params[:query].gsub(' ','+')
    else
      mouse = params[:query]
    end



    system('python python/web_scraper_5.py ' + mouse + ' ' + @latest_id + ' ' + a)
    # system('python python/web_scraper_5.py ' + params[:query] + ' 1')



    redirect_to("/")
  end

  def destroy_newest ### This is used for the homepage
      a = Query.maximum(:id)
      @query = Query.find(a) #could probably write this in one line
      @query.destroy
      @data = Datum.where(:query_id => a)
      @data.destroy_all
      redirect_to("/")
  end

  def destroy_selected ### destroy the item selected (This is used for the show pages)
    a = params[:id]
    @query = Query.find(a) #could probably write this in one line
    @query.destroy
    @data = Datum.where(:query_id => a)
    @data.destroy_all
    redirect_to("/")
  end

end
