class CreateData < ActiveRecord::Migration
  def change
    create_table :data do |t|
      t.integer :query_id
      t.string :word
      t.string :module
      t.integer :freq
      t.decimal :flow

      t.timestamps null: false
    end
  end
end
