<?
  # This PHP script analises HTTP headers trying to understand if the client is hidden behind a proxy server
  # For transparent and anonymous proxy, proxy_detected value is 1.
  # For highly anonymous or elite proxies, proxy_detected is 0.
  #
  # Proxy types:
  #  Transparent - if define any of the vars below or if the client IP
  #  Anonymous - allowed vars HTTP_VIA and HTTP_FORWARDED_FOR if they do not contain client IP
  #  Elite - it does not define any of these vars 

  # Check for Elite proxies
  $TEST = $_SERVER['HTTP_VIA']
  .$_SERVER['HTTP_X_FORWARDED_FOR']
  .$_SERVER['HTTP_FORWARDED_FOR']
  .$_SERVER['HTTP_X_FORWARDED']
  .$_SERVER['HTTP_FORWARDED']
  .$_SERVER['HTTP_CLIENT_IP']
  .$_SERVER['HTTP_FORWARDED_FOR_IP']
  .$_SERVER['VIA']
  .$_SERVER['X_FORWARDED_FOR']
  .$_SERVER['FORWARDED_FOR']
  .$_SERVER['X_FORWARDED']
  .$_SERVER['FORWARDED']
  .$_SERVER['CLIENT_IP']
  .$_SERVER['FORWARDED_FOR_IP']
  .$_SERVER['HTTP_PROXY_CONNECTION'];
  
  $PROXY_DETECTED = (strlen($TEST) ? 1 : 0);

  # prints output in JSON file
  print '{ "proxychecker_version" : "0.1", "ip" : "'.$_SERVER['REMOTE_ADDR'].'", "proxy_detected" : '. $PROXY_DETECTED.' }';

?>
