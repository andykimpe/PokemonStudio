import { Editor } from '@components/editor';
import { EditorHandlingClose, useEditorHandlingClose } from '@components/editor/useHandleCloseEditor';
import { InputWithTopLabelContainer, Label } from '@components/inputs';
import { DbSymbol } from '@modelEntities/dbSymbol';
import { useCreaturePage } from '@utils/usePage';
import { TFunction } from 'i18next';
import React, { forwardRef, useMemo, useState } from 'react';
import { useTranslation } from 'react-i18next';
import { useUpdateForm } from './useUpdateForm';
import { SelectPokemon2 } from '@components/selects/SelectPokemon';
import { SelectCreatureForm } from '@components/selects/SelectPokemonForm';
import { CREATURE_FORM_VALIDATOR } from '@modelEntities/creature';
import { useZodForm } from '@utils/useZodForm';
import { InputFormContainer } from '@components/inputs/InputContainer';
import { useInputAttrsWithLabel } from '@utils/useInputAttrs';

const breedingGroupEntries = [
  'undefined',
  'monster',
  'water_1',
  'bug',
  'flying',
  'field',
  'fairy',
  'grass',
  'human_like',
  'water_3',
  'mineral',
  'amorphous',
  'water_2',
  'ditto',
  'dragon',
  'unknown',
] as const;

const getBreedingGroupOptions = (t: TFunction<'database_pokemon'>) =>
  breedingGroupEntries
    .map((breedingGroup, index) => ({ value: index.toString(), label: t(breedingGroup) }))
    .sort((a, b) => a.label.localeCompare(b.label));

const BREEDING_EDITOR_SCHEMA = CREATURE_FORM_VALIDATOR.pick({
  babyDbSymbol: true,
  babyForm: true,
  breedGroups: true,
  hatchSteps: true,
});

export const BreedingEditor = forwardRef<EditorHandlingClose>((_, ref) => {
  const { t } = useTranslation('database_pokemon');
  const { creature, form } = useCreaturePage();
  const updateForm = useUpdateForm(creature, form);
  const { canClose, getFormData, onInputTouched, defaults, formRef } = useZodForm(BREEDING_EDITOR_SCHEMA, form);
  const { Input, Select } = useInputAttrsWithLabel(BREEDING_EDITOR_SCHEMA, defaults);
  const breedingGroupOptions = useMemo(() => getBreedingGroupOptions(t), [t]);
  const [baby, setBaby] = useState(form.babyDbSymbol);

  const onClose = () => {
    const result = canClose() && getFormData();
    if (result && result.success) updateForm(result.data);
  };
  useEditorHandlingClose(ref, onClose, canClose);

  return (
    <Editor type="edit" title={t('breeding')}>
      <InputFormContainer ref={formRef}>
        <InputWithTopLabelContainer>
          <Label htmlFor="baby">{t('baby')}</Label>
          <SelectPokemon2 name="babyDbSymbol" defaultValue={defaults.babyDbSymbol as DbSymbol} onChange={setBaby} />
        </InputWithTopLabelContainer>
        <InputWithTopLabelContainer>
          <Label htmlFor="form">{t('form')}</Label>
          <SelectCreatureForm dbSymbol={baby} name="babyForm" defaultValue={defaults.babyForm} />
        </InputWithTopLabelContainer>
        <Select name="breedGroups.0" label={t('egg_group_1')} options={breedingGroupOptions} data-input-type="number" />
        <Select name="breedGroups.1" label={t('egg_group_2')} options={breedingGroupOptions} data-input-type="number" />
        <Input name="hatchSteps" label={t('hatch_steps')} labelLeft onInput={onInputTouched} />
      </InputFormContainer>
    </Editor>
  );
});
BreedingEditor.displayName = 'BreedingEditor';
