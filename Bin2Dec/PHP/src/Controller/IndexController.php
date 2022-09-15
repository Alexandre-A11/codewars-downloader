<?php declare(strict_types=1);

namespace App\Controller;

class IndexController extends AbstractController {
    public function Index() {
        if ($_POST) {
            $result = 0;
            for ($i = 0; $i < strlen($_POST["binary"]); $i++) {
                $result += strrev($_POST["binary"])[$i] != 0 ? 2 ** $i : 0;
            }

            parent::render("index", (string) $result);
        }

        parent::render("index");
    }
}
