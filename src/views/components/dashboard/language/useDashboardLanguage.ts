import { useProjectConfigReadonly } from '@utils/useProjectConfig';
import { useProjectStudio } from '@utils/useProjectStudio';
import { useUpdateLanguage } from './editors/useUpdateLanguage';
import { useUpdateGameOptions } from '../gameOptions';
import { useUpdateProjectStudio } from '@utils/useUpdateProjectStudio';
import { cloneEntity } from '@utils/cloneEntity';
import { StudioLanguageConfig } from '@modelEntities/config';

export type DashboardLanguageType = 'translation' | 'player';

const updateDefaultLanguage = (language: StudioLanguageConfig) => {
  if (language.choosableLanguageCode.indexOf(language.defaultLanguage) === -1) {
    language.defaultLanguage = language.choosableLanguageCode[0];
  }
};

export const useDashboardLanguage = () => {
  const { projectConfigValues: language } = useProjectConfigReadonly('language_config');
  const updateLanguage = useUpdateLanguage(language);
  const { projectConfigValues: gameOptions } = useProjectConfigReadonly('game_options_config');
  const updateGameOptions = useUpdateGameOptions(gameOptions);
  const { projectStudioValues: projectStudio } = useProjectStudio();
  const updateProjectStudio = useUpdateProjectStudio(projectStudio);

  const disabledLanguage = (code: string) => {
    if (language.choosableLanguageCode.length <= 1) return;

    const index = language.choosableLanguageCode.indexOf(code);
    if (index === -1) return;

    const languageEdited = cloneEntity(language);
    languageEdited.choosableLanguageCode.splice(index, 1);
    languageEdited.choosableLanguageTexts.splice(index, 1);
    if (languageEdited.choosableLanguageCode.length <= 1) {
      updateGameOptions({ order: gameOptions.order.filter((k) => k !== 'language') });
    }
    updateDefaultLanguage(languageEdited);
    updateLanguage(languageEdited);
  };

  const enableLanguageInGame = (code: string) => {
    const index = projectStudio.languagesTranslation.findIndex(({ code: c }) => c === code);
    if (index === -1) return;

    const otherLanguage = projectStudio.languagesTranslation[index];
    const languageEdited = cloneEntity(language);
    languageEdited.choosableLanguageCode.push(otherLanguage.code);
    languageEdited.choosableLanguageTexts.push(otherLanguage.name);
    if (!gameOptions.order.includes('language')) {
      const order = cloneEntity(gameOptions.order);
      order.unshift('language');
      updateGameOptions({ order });
    }
    updateLanguage(languageEdited);
  };

  const onChangeDefaultLanguage = (defaultLanguage: string) => updateLanguage({ defaultLanguage });

  return {
    languageConfig: language,
    projectStudio,
    gameOptions,
    disabledLanguage,
    enableLanguageInGame,
    onChangeDefaultLanguage,
    updateLanguageConfig: updateLanguage,
    updateGameOptions,
    updateProjectStudio,
  };
};
