 server 'mj-kb2',
   user: 'odoo',
   roles: %w{web app},
   ssh_options: {
     user: 'odoo', # overrides user setting above
     keys: %w(/home/odoo/.ssh/id_rsa),
     forward_agent: false,
     #auth_methods: %w(publickey),
     password: '51448888'
  }

namespace :odoo do
  desc "复制odoo的启动脚本"
  task :setup do
  on roles(:app), in: :sequence, limit: 3, wait: 3 do
    config_file = 'odoo_config_production.erb'
    template config_file, "/tmp/odoo_config", 0750
    sudo "mv /tmp/odoo_config /etc/#{fetch(:application)}.conf"

    template "odoo_server.erb", "/tmp/odoo_server", 0750
    sudo "mv /tmp/odoo_server /etc/init.d/#{fetch(:application)}"
    # restart
   end
  end
  #after "deploy:starting", "odoo:setup"
end