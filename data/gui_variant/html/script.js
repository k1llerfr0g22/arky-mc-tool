function hello_world_js() 
{
  eel.hello_world()  
}

function quit_js()
{
  
  window.close();
  window.stop();
  eel.expose(quit)
  eel.exit()
}

function start_server_2g()
{
  eel.sts2g_thread()
}