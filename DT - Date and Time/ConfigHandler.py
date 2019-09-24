
import configparser
import os


class ConfigHandler(object):

    def __init__(self, config):
        """
        :param config: None or configparser. If None, default configparser 
                       "config.ini" is read from parenct directory.
        """

        if config is None:
            self.config = configparser.ConfigParser()
            par_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
            par_par_dir = os.path.abspath(os.path.join(os.getcwd(), "../.."))

            # FIXME - check this in src configuration
            if par_dir[-3:] == "src":
                self.config.read(os.path.join(par_par_dir, "config.ini"))
            else:
                self.config.read(os.path.join(par_par_dir, "config.ini"))
        else:
            self.config = config


if __name__ == "__main__":
    ch = ConfigHandler(None)

    print(ch.config.get("path", "raw_data_test"))
