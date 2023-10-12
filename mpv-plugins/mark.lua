local mp = require('mp')

require('os')

mp.add_key_binding('n', 'mark-moment', function()
  local current_moment = mp.get_property('playback-time')
  local filename = mp.get_property('filename')
  mp.osd_message("marked")
  os.execute('echo '..filename..' '..current_moment..' >> moments.txt')
end)
