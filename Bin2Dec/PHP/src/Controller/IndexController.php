<?php declare(strict_types=1);

namespace App\Controller;

class IndexController extends AbstractController {
    public function Index() {
        parent::render("index");
    }
}
