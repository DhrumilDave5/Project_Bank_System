import sys
import pygame as pg
import button
import textbox
import interest


def main() -> None:

    pg.init()

    window = pg.display.set_mode((1000, 750))
    pg.display.set_caption("Kendriya National Bank")

    main_clock = pg.time.Clock()

    button1 = button.Button(window, "Calculate", 400, 450, 200, 50)
    buttons: list[button.Button] = [button1, ]
    textbox1 = textbox.TextBox(window, 450, 150, 300, text_allowed="float")
    textbox2 = textbox.TextBox(window, 450, 250, 300, text_allowed="float")
    textbox3 = textbox.TextBox(window, 450, 350, 300, text_allowed="int")
    text_boxes: list[textbox.TextBox] = [textbox1, textbox2, textbox3]

    title_font = pg.font.SysFont("cambria", 60)
    title_to_display = title_font.render("Calculate Simple Interest",
                                         True, (0, 0, 255))
    title_x = (window.get_width() - title_to_display.get_width()) // 2
    result = "Enter values in above fields"

    caption_font = pg.font.SysFont("cambria", 27)
    text_box_caption_1 = \
        caption_font.render("Principal Amount:", True, (255, 0, 0))
    text_box_caption_2 = caption_font.render("Interest Rate (Per Annum):",
                                             True, (255, 0, 0))
    text_box_caption_3 = \
        caption_font.render("Time Period (in Years):", True, (255, 0, 0))

    p, r, t = 0, 0, 0

    window_on = True

    while window_on:

        '''Taking Input'''

        for event in pg.event.get():

            if event.type == pg.QUIT:
                window_on = False

            if event.type == pg.KEYDOWN:
                for i in text_boxes:
                    i.keyboard_input(event)

        for i in text_boxes:
            i.mouse_input()

        for i in buttons:
            i.mouse_input()

        '''Processing'''

        if textbox1.action:
            p = textbox1.give_value()
        if textbox2.action:
            r = textbox2.give_value()
        if textbox3.action:
            t = textbox3.give_value()
        if button1.action:
            if p and r and t:
                result = interest.simple(p, r, t)
            else:
                result = "Enter values in above fields"

        '''Display'''

        window.fill((255, 255, 255))

        for i in buttons:
            i.display()

        for i in text_boxes:
            i.display()

        window.blit(title_to_display, (title_x, 20))
        window.blit(text_box_caption_1, (50, 150))
        window.blit(text_box_caption_2, (50, 250))
        window.blit(text_box_caption_3, (50, 350))
        result_caption = caption_font.render(result, True, (0, 255, 0))
        result_x = (window.get_width() - result_caption.get_width()) // 2
        window.blit(result_caption, (result_x, 550))

        pg.display.flip()

        main_clock.tick(60)

    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
