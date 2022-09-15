<?php declare(strict_types=1);

ini_set("display_errors", 1);
include "../vendor/autoload.php";

$uri = explode("?", $_SERVER["REQUEST_URI"])[0];

$route = require_once "../config/routes.php";

$controllerName = $route[$uri]["Controller"];
$methodName = $route[$uri]["Method"];

(new $controllerName())->$methodName();
// $call = new $controllerName();
// $call->$methodName();
