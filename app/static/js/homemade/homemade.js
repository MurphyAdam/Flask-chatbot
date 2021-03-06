var HomemadeGlobal = {
    navbarBurgers: function() {
        $(".navbar-burger").click((function() {
            var target = $(this).attr("data-target");
            $(this).toggleClass("is-active");
            $(`#${target}`).toggleClass("is-active");
        }));
    },
    formsToggler: function() {
        $(".forms-link").click((function() {
            $(".modal-close").each((function() {
                var target = $(this).attr("data-target");
                if ($(target).hasClass("is-active")) {
                    $(target).removeClass("is-active");
                }
            }));
            var target = $(this).attr("data-target");
            $(target).addClass("is-active");
        }));
        $(".modal-close").click((function() {
            var target = $(this).attr("data-target");
            $(target).removeClass("is-active");
        }));
    },
    removeNotifications: function() {
        $(".notification .delete").click((function() {
            $(this)["0"].parentNode.remove();
        }));
    },
    init: function() {
        HomemadeGlobal.navbarBurgers();
        HomemadeGlobal.formsToggler();
        HomemadeGlobal.removeNotifications();
    }
};

$(document).ready(HomemadeGlobal.init());