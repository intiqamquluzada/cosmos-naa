import { jqueryMinJs } from "../jquery-js/jquery-3.6.0.min.js";
import { jqueryUi } from "../jquery-js/jquery-ui.min.js";

import { btpBundle } from "../bootstrap/bootstrap.bundle.min.js";
import { btpNotify } from "../bootstrap/bootstrap-notify.min.js";
import { btpPopper } from "../bootstrap/popper.min.js";

import { featherMinJs } from "../feather/feather.min.js";
import { featherIcon } from "../feather/feather-icon.js";

import { lazySizes } from "../lazyload/lazysizes.min.js";

import { slickJs } from "../slick/slick.js";
import { slickAnimation } from "../slick/slick-animation.min.js";
import { customAnimated } from "../custom-slick-animated.js";
import { customSlick } from "../slick/custom_slick.js";

jqueryMinJs();
jqueryUi();

btpBundle();
btpNotify();
btpPopper();

featherMinJs();
featherIcon();

lazySizes();

slickJs();
slickAnimation();
customAnimated();
customSlick();