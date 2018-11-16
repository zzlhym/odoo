lock '3.4.0'
set :application, 'mj_oa'
set :repo_url, 'git@git.tongbaner.com:mj/mj_oa.git'
set :deploy_to, "/home/odoo/#{fetch(:application)}"
set :pty, true
set :scm, :git
set :git_strategy, Capistrano::Git::SubmoduleStrategy

set :odoo_pid_file, fetch(:application)
set :odoo_log_file, fetch(:application)
set :odoo_config_file, fetch(:application) 
set :odoo_port, 9002
set :odoo_database, 'mj_oa'
set :templating_paths, ['config/templates']
set :use_sudo, false


set :branch, ENV["BRANCH"] || 'master'

namespace :deploy do

  desc "Makes sure local git is in sync with remote."
  task :restart do
    on roles(:app), in: :sequence, limit: 3, wait: 3 do
      sudo "/etc/init.d/#{fetch(:application)} restart"
    end
  end

  desc "Makes sure local git is in sync with remote."
  task :stop do
    on roles(:app), in: :sequence, limit: 3, wait: 3 do
      sudo "/etc/init.d/#{fetch(:application)} stop"
    end
  end

  after :finishing, :clear_cache do
   on roles(:app), in: :sequence, limit: 3, wait: 3 do
      name = 'openerp-server'
      #execute "ps -ef | grep #{name} | grep -v grep | awk '{print $2}' | xargs kill || echo 'no process with name #{name} found'"
      puts "开始重启odoo"
      puts ('*' * 100)
      sudo "/etc/init.d/#{fetch(:application)} restart"
      puts ('#' * 100)
      puts "成功启动odoo"
    end
  end
end


